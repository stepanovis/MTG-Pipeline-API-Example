import requests

# Параметры
your_api_key = 'fOUbC7xPgpLeGSQlwwHArJXIht0NEOn2TXldaAT9Exp31SEImKTwGgAHZIDeoalh'
biobank_id = 1  # пример: "ATLAS1"
url = f"https://api.hyperunison.com/api/public/cohort/biobank/{biobank_id}/execute-query"

# Чтение YAML-запроса как строки
with open("query.yaml", "r") as f:
    yaml_content = f.read()

# Формирование тела запроса
payload = {
    "yaml": yaml_content,
    "skipCache": False  # или True, если нужно игнорировать кэш
}

headers = {
    "apiKey": your_api_key,
    "accept": "application/json",
    "Content-Type": "application/json"
}

# Выполнение POST-запроса
response = requests.post(url, json=payload, headers=headers)

# Печать результата
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
