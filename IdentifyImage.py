import requests
import shutil
import json 

files = {'imag': open('sendFile.jpg', 'rb')}
url = 'https://www.wolframcloud.com/objects/martinsiby/IdentifyImage'
print(files)
r = requests.post(url, files=files)
print (r.text)
d = list(r.text)
iterate=0
category=0
string='{\'Category\': \''
while(iterate<len(d)):
	if(d[iterate]=="\""):
		iterate+=1
		while(d[iterate]!='\"' and d[iterate]!=':'):
			string+=d[iterate]
			iterate+=1
		if(category==0):
			string+='\', \'object\' : \''
		else:
			string+='\'}'
			break;
		category=1
	iterate+=1	
n = json.dumps(string)
JsonObj = json.loads(n)
print(string)
