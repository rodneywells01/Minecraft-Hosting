from discord_bot import bot
import re

def test_token_fetch():
    print("Mock Test")

def test_message_filtering():
    mock_messages = {
        "hello": "hello",
        "<@1123123>hello1": "hello1",
        "<@1123123> hello1": "hello1",
        "<@1123123>     ": "",
        "<@1232132><@Swag> Test": "test"
    }

    for message in mock_messages:
        assert bot.cleanse_message(message) == mock_messages[message]

