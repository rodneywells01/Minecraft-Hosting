docker kill $(docker ps -aqf "name=minecraft-server")
docker rm minecraft-server


# Manual Run Command 
# docker run -p 25565:25565 --name minecraft-server --entrypoint '/bin/sh'  rodneywells01/minecraft-server:velvety-run -c './scripts/deploy_minecraft.sh'
