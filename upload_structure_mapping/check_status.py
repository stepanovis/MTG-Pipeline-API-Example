import requests
import json


# Biobank code
biobank_code = 'YAMLEXMPL'

# Your API key
api_key = 'fOUbC7xPgpLeGSQlwwHArJXIht0NEOn2TXldaAT9Exp31SEImKTwGgAHZIDeoalh'

# Endpoint URL
url = f'https://api.hyperunison.com/api/public/structure/{biobank_code}/status'

# Make GET request
response = requests.get(
    url,
    headers={
        'apiKey': api_key
    }
)

# Print status and response
print(response.status_code)
print(json.dumps(response.json(), indent=2, ensure_ascii=False))
