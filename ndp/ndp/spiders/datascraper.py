import scrapy
from config import mappings, year
import json
from html_to_json import convert_to_json


class DatascraperSpider(scrapy.Spider):
    name = "datascraper"
    allowed_domains = ["nationaldata.gov.np"]
    data_list = []

    def start_requests(self):
        # handle_httpstatus_list for handling 500 internal server error which occurs when page number exceeds the number of pages of data that are available
        for province, districts in mappings[0].items():
            for district, municipalities in districts.items():
                for municipality, code in municipalities.items():
                    yield scrapy.Request(f'http://nationaldata.gov.np/LocalLevel/GetData?id={code}&tgid=0&tsgid=0&tid=0&year={year}&tempTitle=&pageNo=1', callback=self.parse, meta={'id': code, 'district': district, 'municipality': municipality, "province": province, "year": year, 'handle_httpstatus_list': [500]})

    def parse(self, response):
        # access relevant data from meta passed above
        id = response.meta['id']
        district = response.meta['district']
        municipality = response.meta['municipality']
        province = response.meta['province']
        year = response.meta['year']

        # try to access page_number, if not available set to 1
        page_number = response.meta.get('page_number', 1)

        # when there are no more data availabe, we get 'Data not available.' in response
        no_content = response.css(
            'div.col-sm-12 div.panel div.panel-body h4::text').get()

        # select all tables
        tables = response.css('table.table')

        # convert html table to json
        for indv_table in tables:
            data_dict = convert_to_json(
                indv_table.get(), province, district, municipality)

            self.data_list.append(data_dict)

        # if there is more data keep sending request by incrementing page_number else stop sending request
        if no_content != "Data not available.":
            page_number += 1
            yield scrapy.Request(f'http://nationaldata.gov.np/LocalLevel/GetData?id={id}&tgid=0&tsgid=0&tid=0&year={year}&tempTitle=&pageNo={page_number}', meta={'page_number': page_number, 'id': id, 'district': district, 'municipality': municipality, 'province': province, 'year': year, 'handle_httpstatus_list': [500]}, callback=self.parse)
        else:
            return

    def closed(self, reason):
        with open(f'national_data_profile_year_{year}.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.data_list, json_file, ensure_ascii=False, indent=4)
