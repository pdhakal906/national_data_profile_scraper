import json
import re
from bs4 import BeautifulSoup
html = '''      <table class="table table-condensed table-striped" id="Table_5006">
      <tr>
        <th>Educational Institutions</th>
        <th style="text-align:right">Number</th>
      </tr>
      <tr>
        <td class="col-sm-8">College/University</td>
        <td class="col-sm-2" style="text-align:right;">2</td>
      </tr>
      <tr>
        <td class="col-sm-8">Basic Level</td>
        <td class="col-sm-2" style="text-align:right;">10</td>
      </tr>
      <tr>
        <td class="col-sm-8">Secondary Level</td>
        <td class="col-sm-2" style="text-align:right;">12</td>
      </tr>
      <tr>
        <th>Number of students</th>
        <th></th>
      </tr>
      <tr>
        <td class="col-sm-8">Secondary Level</td>
        <td class="col-sm-2" style="text-align:right;">566</td>
      </tr>
      <tr>
        <td class="col-sm-8">College/University</td>
        <td class="col-sm-2" style="text-align:right;">400</td>
      </tr>
      <tr>
        <td class="col-sm-8">Basic Level</td>
        <td class="col-sm-2" style="text-align:right;">799</td>
      </tr>
      <tr>
        <th>Number of teaching staffs</th>
        <th></th>
      </tr>
      <tr>
        <td class="col-sm-8">Secondary Level</td>
        <td class="col-sm-2" style="text-align:right;">355</td>
      </tr>
      <tr>
        <td class="col-sm-8">College/University</td>
        <td class="col-sm-2" style="text-align:right;">115</td>
      </tr>
      <tr>
        <td class="col-sm-8">Basic Level</td>
        <td class="col-sm-2" style="text-align:right;">12</td>
      </tr>
      <tr>
        <th>Number of non- teaching staffs</th>
        <th></th>
      </tr>
      <tr>
        <td class="col-sm-8">Basic Level</td>
        <td class="col-sm-2" style="text-align:right;">115</td>
      </tr>
      <tr>
        <td class="col-sm-8">College/University</td>
        <td class="col-sm-2" style="text-align:right;">11</td>
      </tr>
      <tr>
        <td class="col-sm-8">Secondary Level</td>
        <td class="col-sm-2" style="text-align:right;">11</td>
      </tr>
    </table>'''

soup = BeautifulSoup(html, 'html.parser')

# Find the table element
table = soup.find('table')

# Initialize an empty dictionary to store the JSON data
result = {}

# Initialize a stack to keep track of the current dictionary
stack = [result]

# Iterate through each row in the table
for row in table.select('tr'):
    headers = row.select('th')  # Select all th elements in the row
    data_cells = row.select('td')  # Select all td elements in the row

    # Check if the row contains headers
    if headers:
        # Use the text content of the first th as the key
        current_key = headers[0].text.strip()
        new_dict = {}  # Initialize an empty dictionary for the current key
        stack[-1][current_key] = new_dict
        stack.append(new_dict)

    # Check if the row contains data cells
    elif data_cells:
        # Use the text content of the first td as the key
        key = data_cells[0].text.strip()
        stack[-1][key] = {
            'Number': data_cells[1].text.strip(),

        }

    # If neither headers nor data cells are found, pop the stack
    else:
        stack.pop()

# Convert the result dictionary to JSON
json_result = json.dumps(result, indent=2)

# Print the JSON data
print(json_result)
