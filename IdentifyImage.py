import requests
import json 

files = {'image': open('sendFile.jpg', 'rb')}
url = 'https://www.wolframcloud.com/objects/martinsiby/IdentifyImage'
r = requests.post(url, files=files)
JsonObj = json.loads(r.text)
print(JsonObj["Result"])

