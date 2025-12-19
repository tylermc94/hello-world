import requests
import json
#needs a config.py file with the following variables for sensitive data
from config import PIHOLE_ADDR, PIHOLE_API_TOKEN

# Set up auth variables
auth_url = f"https://{PIHOLE_ADDR}/api/auth"
api_key = {"password": PIHOLE_API_TOKEN}

# Make the auth request
auth_response = requests.post(auth_url, json=api_key, verify=False)

# Parse the JSON response
auth_data = auth_response.json()

# Uncomment next line to see the auth output
# print(auth_data)

# Extract the sid
sid = auth_data["session"]["sid"]
csrf = auth_data["session"]["csrf"]

# Uncomment next two lines to see the sid and csrf tokens
#print(sid)
#print(csrf)

# Now use it in your next request

top_domains_url = f"https://{PIHOLE_ADDR}/api/stats/top_domains"
headers = {
  "X-FTL-SID": sid,
  "X-FTL-CSRF": csrf
}
top_domains = requests.request("GET", top_domains_url, headers=headers, verify=False)

print(top_domains.json())

with open("top_domains.json", "w") as final:
        json.dump(top_domains.json(), final)  

def output_table(top_domains):
  data = top_domains.json()
  print(f"{'Domain':<50} {'Count':>10}")
  print("-" * 60)
  for item in data["domains"]:
    print(f"{item['domain']:<50} {item['count']:>10}")

output_table(top_domains)