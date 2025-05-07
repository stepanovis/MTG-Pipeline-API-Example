import subprocess
import json

your_api_key = 'gb6mFnl801aplGGljHQ2PO4EUOzlsVo3zA2AzJMfKp7UzjAJfU0VerInz029K3Uw'

def run_curl(api_key: str):
    cohort_query = """SELECT:
  - c1.name
  - c2.name
  - gender
  - race
  - year_of_birth

FROM: [UKBB1, ATLAS1]

JOIN:
  - condition_occurrence: c1
  - drug_exposure: d1_line1
  - drug_exposure: d1_line2
  - condition_occurrence: c2
  - drug_exposure: d2

WHERE:
  - c1.name IN ["Rheumatoid arthritis, unspecified"]
  - d1_line1.name IN ["Methotrexate", "Hydroxychloroquine", "Sulfasalazine", "Leflunomide"]
  - d1_line1.start_date > c1.start_date and c1.end_date + 90 days > d1_line1.end_date
  - d1_line2.name IN ["Adalimumab", "Etanercept", "Infliximab", "Golimumab"]
  - d1_line2.start_date > d1_line1.end_date and c1.end_date + 90 days > d1_line2.end_date
  - c2.name IN ["Cardiovascular disease, unspecified"]
  - c2.start_date > c1.start_date
  - d2.name IN ["Statins (HMG-CoA reductase inhibitors)", "BETA BLOCKERS/RELATED"]
  - d2.start_date > c2.start_date
  - d2.start_date < c2.end_date + 90 days

LIMIT: 500
"""

    payload = {
        "parameters": {},
        "biobanks": ["UKBB1", "ATLAS1"],
        "cohort": cohort_query,
        "project": None
    }

    payload_str = json.dumps(payload)
    cmd = f"""curl -X POST \
-H "apiKey: {api_key}" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
--data '{payload_str}' \
https://api.hyperunison.com/api/public/pipeline/workflow/run/10/"""

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print("Status:", result.returncode)
    print("Output:", result.stdout)
    print("Error:", result.stderr)


# Пример вызова
run_curl(your_api_key)