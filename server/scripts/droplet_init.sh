docker pull rodneywells01/minecraft-server
docker pull rodneywells01/minecraft-api
docker run \
    --detach \
    -p 25565:25565 \
    --name minecraft-server \
    --volume server-data:server-data
    rodneywells01/minecraft-server