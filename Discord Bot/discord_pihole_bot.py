# This example requires the 'message_content' intent.

import discord
import requests
import urllib3
#needs a config.py file with the following variables for sensitive data
from config import discord_test_bot_token, PIHOLE_ADDR, PIHOLE_API_TOKEN

#disable tls warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sid = ""
csrf = ""
auth_success = ""

# Set Functions

def pihole_auth(): #Authenticate to pihole and return sid and csrf tokens
    # Set up auth variables
    auth_url = f"http://{PIHOLE_ADDR}/api/auth"
    api_key = {"password": PIHOLE_API_TOKEN}
    auth_response = requests.post(auth_url, json=api_key, verify=False)

    # Parse the JSON response
    auth_data = auth_response.json()

    if auth_response.status_code == 200:
        global auth_success
        auth_success = True

    # Uncomment next line to see the auth output
    #print(auth_data)

    # Extract the sid
    global sid
    global csrf
    sid = auth_data["session"]["sid"]
    csrf = auth_data["session"]["csrf"]

def pihole_status():
    status_url = f"http://{PIHOLE_ADDR}/api/stats/summary"
    headers = {
        "X-FTL-SID": sid,
        "X-FTL-CSRF": csrf
    }
    pihole_status = requests.request("GET", status_url, headers=headers, verify=False)
    data = pihole_status.json()
    
    # Now just access and print the values you want
    status_message = "=== Pi-hole Status ===\n"
    # Extract relevant queries
    total_queries = data["queries"]["total"]
    blocked_queries = data["queries"]["blocked"]
    percent_blocked = round(data["queries"]["percent_blocked"], 1)
    active_clients = data["clients"]["active"]
    total_clients = data["clients"]["total"]
    # Print them with nice formatting
    status_message += f"Total Queries: {total_queries}\n"
    status_message += f"Blocked Queries: {blocked_queries}\n"
    status_message += f"Percent Blocked: {percent_blocked}%\n"
    status_message += "-" * 60 + "\n"
    status_message += f"Total Clients: {total_clients}\n"
    status_message += f"Active Clients: {active_clients}\n"

    return status_message

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    pihole_auth()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    pihole_auth()
    if auth_success == True:
        print(f"\nSuccessfully authenticated to http://{PIHOLE_ADDR}/api")
    else:
        print(f"\nFailed to authenticate to http://{PIHOLE_ADDR}/api")
    

@client.event
async def on_message(message): # Listen for messages and respond accordingly
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$pihole-status'):
        status = pihole_status()
        await message.channel.send(status)

client.run(discord_test_bot_token)