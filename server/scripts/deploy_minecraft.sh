echo "Launching the Boolean Boys Minecraft Server"

# Pull and run the latest minecraft server.
./scripts/pull-world.sh
java -Xmx2048M -Xms2048M -jar server.jar nogui