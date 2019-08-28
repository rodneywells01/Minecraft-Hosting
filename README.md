# Minecraft-Hosting
Easy deployment and configuration of a Minecraft Server


### Deploying the latest version of the minecraft server.
```
docker pull rodneywells01/minecraft-server
docker run --detach --name minecraft-server rodneywells01/minecraft-server
```

That's it. Server is now up.

### Pushing a newer version of the server.
```
docker-compose build
./scripts/push-image.sh
```

You'll need my registry password for now to get access to the DockerHub Repo. Talk to me about permissions.

### Configuring the server
Everything can be found in the `server.properties` file.