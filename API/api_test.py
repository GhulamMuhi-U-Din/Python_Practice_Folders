import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)

# print JSON response 

response = requests.get("https://api.github.com")

print(response.json())

# text

response = requests.get("https://api.github.com")

print(response.text)