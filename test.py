import requests
import json

url = "http://localhost/api/move"
data = {"pins": [12, 26, 14, 20]}

response = requests.post(url, json=data)

print(response.status_code)
print(response.text)