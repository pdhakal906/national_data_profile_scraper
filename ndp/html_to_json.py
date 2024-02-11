from bs4 import BeautifulSoup


def convert_to_json(html_table, province, district, level):
    soup = BeautifulSoup(html_table, 'html.parser')
    table = soup.find('table')

    result = {
        province: {
            district: {
                level: {}
            }
        }
    }

    stack = [result[province][district][level]]

    for row in table.select('tr'):
        headers = row.select('th')
        data_cells = row.select('td')

        if headers:
            current_key = headers[0].text.strip()
            new_dict = {}
            stack[-1][current_key] = new_dict
            stack.append(new_dict)
        elif data_cells:
            key = data_cells[0].text.strip()
            stack[-1][key] = {
                'Number': data_cells[1].text.strip(),
            }
        else:
            stack.pop()

    return result

    # Print the JSON data
    # print(json_result)
