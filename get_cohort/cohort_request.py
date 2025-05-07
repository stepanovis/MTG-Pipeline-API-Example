from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

your_api_key = 'fOUbC7xPgpLeGSQlwwHArJXIht0NEOn2TXldaAT9Exp31SEImKTwGgAHZIDeoalh'

query = ('CDM: OMOP:5.4\n')
query += 'SELECT:\n'
query += ' - gender\n'
query += ' - race\n'
query += ' - year_of_birth\n\n'
query += 'FROM: [ATLAS1]\n\n'
query += 'LIMIT: 500\n'
biobank_id = '1'

api = UnisonSDKApi(
    Configuration(
        host='https://api.hyperunison.com/',
    )
)
response = api.execute_cohort_request(
    your_api_key,
    biobank_id,
    query
)

print(response)
