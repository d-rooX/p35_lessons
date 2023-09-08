import requests

url = "https://p35api.droox.dev/users"

# response = requests.post(url, params={'name': 'Daniel', 'age': 20})
response = requests.get(url)
data = response.json()
print(data)
# print(data[0]['buy'])
