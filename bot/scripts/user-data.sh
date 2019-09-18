#!/bin/bash

# Pull and start bot
sudo docker pull rodneywells01/minecraft-discord-bot:latest
sudo docker run --detach --name minecraft-discord-bot rodneywells01/minecraft-discord-bot:latest


sudo docker run --name minecraft-discord-bot rodneywells01/minecraft-discord-bot:latest