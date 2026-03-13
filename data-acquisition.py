import requests
import pandas as pd
from credentials import ACCESS_TOKEN
import time

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

url = "https://www.strava.com/api/v3/athlete/activities"

activities = []
page = 1

while True:

    params = {
        "per_page": 200,  # max allowed by API
        "page": page
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("API error:", response.json())
        break

    data = response.json()

    # break once the data has all been gathered
    if not data:
        break

    for activity in data:

        photo_count = activity.get("total_photo_count", 0)

        activities.append({
            "activity_id": activity["id"],
            "name": activity["name"],
            "date": activity["start_date_local"],
            "distance": activity["distance"],              # meters
            "moving_time": activity["moving_time"],        # seconds
            "kudos_count": activity["kudos_count"],        # number of kudos
            "photo_count": photo_count,
            "has_photo": 1 if photo_count > 0 else 0
        })

    page += 1
    time.sleep(0.5)

# save as df
df = pd.DataFrame(activities)
print(df.head())

# data cleaning
data = df
data["distance"] = data["distance"] / 1609.34
data['date'] = pd.to_datetime(data['date']).dt.date

# save to csv
data.to_csv("strava_kudos_data.csv", index=False)