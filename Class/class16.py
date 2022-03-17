import requests

request = requests.options("http://999.md")
print(request.content)
