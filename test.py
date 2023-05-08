import requests
import json
import http.client
import urllib.parse

url = "https://gorest.co.in/public/v2/users"

response = requests.get(url)

response_json = response.json()

data = []

for user in response_json:
    data.append({'name': user['name'], 'email': user['email']})

print(data)
