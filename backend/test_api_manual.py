import requests
import json

death_record = {
    "record_id": "CDR001",
    "name": "राम कुमार शर्मा",
    "father_name": "श्री मोहन लाल शर्मा",
    "date_of_death": "2023-03-15",
    "age": 67,
    "gender": "M",
    "district": "रायपुर",
    "village": "खमतराई",
    "registration_date": "2023-03-18"
}

response = requests.post(
    "http://127.0.0.1:10000/api/beneficiary/discover",
    json=death_record
)

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=2, ensure_ascii=False))