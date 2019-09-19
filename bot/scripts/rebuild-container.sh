docker build . --tag rodneywells01/minecraft-discord-bot:latest
docker kill minecraft-discord-bot
docker rm minecraft-discord-bot
docker run --name minecraft-discord-bot rodneywells01/minecraft-discord-bot:latest
