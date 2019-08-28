# Fetch latest version of Minecraft Server
curl -o server/server.jar https://launcher.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar

# Start the server
java -Xmx1024M -Xms1024M -jar server/server.jar nogui

