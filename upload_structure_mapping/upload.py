import requests

# Путь к вашему YAML файлу
yaml_file_path = 'structure-mapping.yaml'

# Читаем YAML как строку
with open(yaml_file_path, 'r') as f:
    yaml_content = f.read()
# Ваш API-ключ
your_api_key = 'fOUbC7xPgpLeGSQlwwHArJXIht0NEOn2TXldaAT9Exp31SEImKTwGgAHZIDeoalh'

# URL вашего API
url = 'https://api.hyperunison.com/api/public/structure/save'



# Формируем тело запроса
payload = {
    "yaml": yaml_content
}

# Отправляем запрос
response = requests.post(
    url,
    headers={
        'Content-Type': 'application/json',
        'apiKey': your_api_key
    },
    json=payload
)

# Выводим ответ
print(response.status_code)
print(response.json())