import time

def my():

	import requests
	from requests.structures import CaseInsensitiveDict
	
	url = "http://bongotech24lab.xyz//checkadmov/app/api/task-authh.php?user=YzhiZmY1N2M2MDZmNDVmYWIwMzMwNzgyMDYzNjIyM2MyM2ZmZjZkNg==&did=8b2f796f3389516f&&task_api=1234"
	
	headers = CaseInsensitiveDict()
	headers["User-Agent"] = "Dalvik/2.1.0 (Linux; U; Android 11; SM-A107F Build/RP1A.200720.012)"
	headers["Host"] = "bongotech24lab.xyz"
	headers["Connection"] = "Keep-Alive"
	headers["Accept-Encoding"] = "gzip"
	
	
	resp = requests.get(url, headers=headers)
	


def claim(user,aid):

	import requests
	from requests.structures import CaseInsensitiveDict
	
	url = "http://bongotech24lab.xyz//checkadmov/app/api/task-authh.php?user="+user+"&did="+aid+"&&task_api=1234"
	
	headers = CaseInsensitiveDict()
	headers["User-Agent"] = "Dalvik/2.1.0 (Linux; U; Android 11; SM-A107F Build/RP1A.200720.012)"
	headers["Host"] = "bongotech24lab.xyz"
	headers["Connection"] = "Keep-Alive"
	headers["Accept-Encoding"] = "gzip"
	
	
	resp = requests.get(url, headers=headers)
	
	return resp.text



a=input("Enter user :")
b=input("Enter aid :")
c=int(input("Enter claim amount :"))


for i in range(c):
	my()
	x=claim(a,b)
	print(" • "+str(i+1)+" No Click : "+x+"")
	time.sleep(210)

