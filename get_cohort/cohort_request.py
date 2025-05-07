from hyperunison_public_api import UnisonSDKApi
from hyperunison_public_api import Configuration

your_api_key = 'gb6mFnl801aplGGljHQ2PO4EUOzlsVo3zA2AzJMfKp7UzjAJfU0VerInz029K3Uw'

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
