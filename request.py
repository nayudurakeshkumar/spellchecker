import requests
import json
url = 'http://127.0.0.1:8000/spell_checker'
headers = {
    'accept': 'application/json'
}
params = {
    'text': 'Helo. How ar yu?'
}

response = requests.post(url, headers=headers, data=json.dumps(params))

print(response.json())