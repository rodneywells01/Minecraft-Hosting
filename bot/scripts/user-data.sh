# Install Docker
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user

# Pull and start bot
sudo docker pull rodneywells01/minecraft-discord-bot:latest
sudo docker run --detach --name minecraft-discord-bot rodneywells01/minecraft-discord-bot:latest