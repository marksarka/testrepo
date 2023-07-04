import requests

# Replace with your actual Postman API key
api_key = 'c0a8d9f2-8e39-461d-a4eb-3f5d3fc3c1a6'

url = 'https://api.getpostman.com/collections'

headers = {
    'X-Api-Key': api_key
}

response = requests.get(url, headers=headers)

print(response.json())
