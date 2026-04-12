import requests
import json

filename = "wsaa-code.json"

url = 'https://api.github.com/repos/andrewbeattycourseware/wsaa-course-material/contents/code'

response = requests.get(url)
print (response.status_code)
repoJSON = response.json()
#print (response.json())

with  open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)
