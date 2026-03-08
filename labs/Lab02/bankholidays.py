# This program prints the JSON in the url to the console
# Author: Orla Woods

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data['northern-ireland']['events'][0]) # prints the title of the first event in the northern ireland bank holidays list