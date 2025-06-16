import json
import random
import time

def generate_data():
    data = []
    for _ in range(10):
        point = {
            "lat": -5.0 + random.uniform(-0.5, 0.5),
            "lng": 120.0 + random.uniform(-0.5, 0.5),
            "temperature": round(random.uniform(25, 30), 2),
            "current": round(random.uniform(0.5, 2.0), 2),
            "sonar_signal": random.choice([True, False])
        }
        data.append(point)
    return data

def save_to_json():
    fish_data = {
        "locations": generate_data()
    }
    with open("data/fish_data.json", "w") as f:
        json.dump(fish_data, f, indent=2)

if __name__ == "__main__":
    while True:
        save_to_json()
        print("Dummy data updated.")
        time.sleep(10)
