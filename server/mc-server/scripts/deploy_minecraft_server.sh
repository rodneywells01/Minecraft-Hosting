echo "Launching the Minecraft Server"

# Pull and run the latest minecraft server.
./scripts/pull-world.sh
java -Xmx3072M -Xms3072M -jar server.jar nogui