import requests

# Замените URL на адрес вашего Rasa API
url = 'http://localhost:5005/webhooks/rest/webhook'

# Отправьте запрос для начала диалога
response = requests.post(url, json={'message': 'Lord'})
print(response.json())

# Отправьте запрос для продолжения диалога
response = requests.post(url, json={'message': 'What you know about Redis?'})
print(response.json())
