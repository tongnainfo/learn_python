import requests
request=requests.get("http://www.yingjobs.com")
print(request.status_code);
print(request.text)
