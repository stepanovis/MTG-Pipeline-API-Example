import requests

your_api_key = 'fOUbC7xPgpLeGSQlwwHArJXIht0NEOn2TXldaAT9Exp31SEImKTwGgAHZIDeoalh'


# Подгружаем YAML как строку
with open("query.yaml", "r") as f:
    cohort_yaml = f.read()

# Собираем тело запроса
payload = {
    "parameters": {"phenotype": "year_of_birth"},
    "biobanks": ["ATLAS1"],
    "cohort": cohort_yaml,
    "project": "test"
}

headers = {
    "apiKey": your_api_key,
    "accept": "application/json",
    "Content-Type": "application/json"
}

url = "https://api.hyperunison.com/api/public/pipeline/workflow/run/10/"
response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.json())
