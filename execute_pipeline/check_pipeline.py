import requests

your_pipeline_id = 225 #get it from the execution response
your_api_key = "fOUbC7xPgpLeGSQlwwHArJXIht0NEOn2TXldaAT9Exp31SEImKTwGgAHZIDeoalh"

def check_pipeline_status(api_key: str, pipeline_id: int):
    url = f"https://api.hyperunison.com/api/public/pipeline/{pipeline_id}"
    headers = {
        "apiKey": api_key,
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    print("Status:", response.status_code)
    print("Response:", response.json())

# Пример вызова
check_pipeline_status(your_api_key, your_pipeline_id)