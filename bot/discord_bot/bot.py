"""
Discord Bot for Minecraft Server Orchestration

# TODO - Gotta be a cleaner way of doing this....
"""

from google.cloud import storage
import discord

# Fetch Discord token.
def fetch_discord_token():
    """
    Obtain the Discord Token from GCP Storage
    """
    gcp_client = storage.Client()
    bucket = gcp_client.get_bucket('discord-server-bucket')
    blob = bucket.get_blob('discord-key.txt')
    return blob.download_as_string().strip().decode("utf-8")

def help_menu():
    """
    Generate a help menu.
    """
    return "".join([
        "`!help` - Display this menu \n",
        "`!start` - Launch the Minecraft Server, if it's not already running. \n",
        "`!kill` - Requires Admin passcode. Backup and kill the Minecraft server. \n",
        "`!about` - Display some basic info about this bot. \n"
        "`!status` - Get the current status of the Minecraft Server. \n"
    ])

def not_ready():
    return "Sorry! This feature isn't ready yet. Check back soon. :wink:"

def about():
    return "This bot was built by Rodney Wells. You can use it to start the Minecraft server if it is offline."

def invalid_option():
    return "Not a valid option. Try `help`."

possible_responses = {
    "!help": help_menu(),
    "!start": not_ready(),
    "!kill": not_ready(),
    "!about": about(),
    "!status": not_ready()
}

client = discord.Client()

@client.event
async def on_message(message):
    """
    Discord Message event. Triggers for all messages.
    """
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Respond given the contents of a message.
    print(message.content)
    if message.content.startswith("!"):
        message_text = message.content.lower().strip()
        if message_text in possible_responses:
            print("Sending!")
            await message.channel.send(possible_responses[message_text])
        else:
            await message.channel.send(invalid_option())

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
    TOKEN = fetch_discord_token()
    print(TOKEN)
    print(type(TOKEN))
    if not TOKEN:
        raise Exception("Could not fetch Discord Token")
    client.run(TOKEN)
