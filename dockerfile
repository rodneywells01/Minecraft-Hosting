FROM openjdk:latest
WORKDIR /app
COPY ./scripts ./scripts
COPY ./server ./server

RUN yum -y install unzip


# Pull the latest server version
RUN ./scripts/fetch-latest-server.sh

# Start Server
CMD ./scripts/deploy_minecraft.sh