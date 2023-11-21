import requests
import json
import pandas as pd

# Download the JSON file
url = "https://raw.githubusercontent.com/neetcode-gh/leetcode/main/.problemSiteData.json"
response = requests.get(url)
json_data = response.json()

# Filter the entries
filtered_data = []
for entry in json_data:
    if not entry.get("neetcode150") or not entry.get("blind75"):
        filtered_data.append({"code": entry["code"], "link": entry["link"], "video": entry["video"], "pattern": entry["pattern"]})

# Save the filtered data to a CSV file
df = pd.DataFrame(filtered_data)
df.to_csv("filtered_data.csv", index=False)

# Filter the entries
filtered_data = []
for entry in json_data:
    if entry.get("neetcode150"):
        filtered_data.append({"code": entry["code"], "link": entry["link"], "video": entry["video"], "pattern": entry["pattern"]})

# Save the filtered data to a CSV file
df = pd.DataFrame(filtered_data)
df.to_csv("filtered_data_150.csv", index=False)