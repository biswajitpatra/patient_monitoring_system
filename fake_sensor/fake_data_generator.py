import requests
import time
import random
import os

if int(os.environ.get('START')) == 0:
    exit()

while True:
    try:
        types = requests.get("http://server:8000/api/measurements/?format=json")
        break
    except:
        print("retrying")
        time.sleep(1)

types = types.json()

print("STARTING DATA GENERATION ")
patient_tokens = ["edf6a6492d02c41e5bf13752a6a49166af40b7f6"]
while True:
    time.sleep(2)
    for token in patient_tokens:
        data = []
        for type in types:
            data.append(
                {
                    "value": random.uniform(type["min_range"], type["max_range"]),
                    "measurement_type": type["id"],
                }
            )
        requests.post(
            "http://server:8000/api/sensor-data/",
            headers={"Authorization": f"Token {token}"},
            json={"records": data},
        )
