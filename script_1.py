import requests
import pandas as pd

# NSE API URL for Option Chain (Change symbol if needed)
url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en",
    "Referer": "https://www.nseindia.com/"
}

# Start session
session = requests.Session()
session.get("https://www.nseindia.com", headers=headers)  # Set cookies

# Fetch data from NSE API
response = session.get(url, headers=headers)
data = response.json()

# Extract expiry dates
expiry_dates = data["records"]["expiryDates"]

# Generate expiry transition names
expiry_transitions = []
for i in range(len(expiry_dates)):
    for j in range(i + 1, len(expiry_dates)):
        expiry_transitions.append(f"Expiry{i+1}_{j+1}")

# Convert to Pandas DataFrame
df = pd.DataFrame(expiry_transitions, columns=["Expiry Transitions"])

# Display the DataFrame
print(df)

# Save to CSV file (optional)
df.to_csv("expiry_transitions.csv", index=False)
