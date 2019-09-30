"""
Discord Bot for Minecraft Server Orchestration

# TODO - Gotta be a cleaner way of doing this....
"""

from google.cloud import storage
import discord
import re
import requests

# Fetch Discord token.
def fetch_token(blob_name):
    """
    Obtain the Discord Token from GCP Storage
    """
    gcp_client = storage.Client()
    bucket = gcp_client.get_bucket('discord-server-bucket')
    blob = bucket.get_blob(blob_name)
    return blob.download_as_string().strip().decode("utf-8")

def help_menu():
    """
    Generate a help menu.
    """
    return "".join([
        "`help` - Display this menu \n",
        "`start` - Launch the Minecraft Server, if it's not already running. \n",
        "`kill` - Requires Admin passcode. Backup and kill the Minecraft server. \n",
        "`about` - Display some basic info about this bot. \n"
        "`status` - Get the current status of the Minecraft Server. \n"
    ])

def not_ready():
    return "Sorry! This feature isn't ready yet. Check back soon. :wink:"

def about():
    return "This bot was built by Rodney Wells. You can use it to start the Minecraft server if it is offline."

def invalid_option():
    return "Not a valid option. Try `help`."

def get_status():
    """
    Fetch information about the Minecraft server.
    """
    ip = "67.205.169.52" # TODO: dynamic IP Fetch
    url = f"https://mcapi.us/server/status?ip={ip}"
    headers = {
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }
    response = requests.get(url, headers=headers)

    # Handle possible errors in communicaiton.
    if response.status_code != 200:
        message = "Failure to communication with MCAPI. Rodney will dig into this."

    if response.json()["status"] == "error":
        # The server is not up yet.
        message = "The Boolean Boys Minecraft Server is down. You can use `start` to spin the server up!"
    elif response.json()["status"] == "success":
        if not response.json()["online"]:
            message = "The server appears to be unavailable. Please wait."
        else:
            message = "The server is up! Come play!"
            player_count = response.json()["players"]["now"]
            if player_count > 0:
                message += f"\n\n There are **{player_count} players** currently on the server."

    return message

possible_responses = {
    "help": help_menu,
    "start": not_ready,
    "kill": not_ready,
    "about": about,
    "status": get_status
}

client = discord.Client()

def cleanse_message(message_text):
    """
    Clean up a message
    """

    # Get lower
    message_text = message_text.lower()

    # Remove mentions
    message_text = re.sub("<@.*?>", "", message_text)

    # Delete whitespace
    message_text = message_text.strip()

    return message_text


async def respond(message):
    """
    Issue a response to a message.
    """
    message_text = cleanse_message(message.content)
    if message_text in possible_responses:
        await message.channel.send(possible_responses[message_text]())
    else:
        await message.channel.send(invalid_option())

@client.event
async def on_message(message):
    """
    Discord Message event. Triggers for all messages.
    """
    # we do not want the bot to reply to itself
    # print(message.author)
    # print(client.user)
    # print(message.mentions)
    if message.author == client.user:
        return

    for mention in message.mentions:
        if mention.name == client.user.name:
            await respond(message)


@client.event
async def on_ready():
    """
    Initial Discord Bot Instantiation
    """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if  __name__ == "__main__":
    DISCORD_TOKEN = fetch_token('discord-key.txt')
    DIGITAL_OCEAN_TOKEN = fetch_token('digital-ocean-key.txt')

    if any([not DISCORD_TOKEN, not DIGITAL_OCEAN_TOKEN]):
        raise Exception("Could not fetch token")
    client.run(DISCORD_TOKEN)
