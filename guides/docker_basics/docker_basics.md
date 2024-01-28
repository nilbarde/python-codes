# Docker Basics Guide

This guide provides a quick reference for getting started with Docker on Ubuntu. Docker is a platform for developing, shipping, and running applications in containers.

## Table of Contents

1. [Installing Docker](#1-installing-docker)
2. [Running Your First Container](#2-running-your-first-container)
3. [Building Docker Images](#3-building-docker-images)
4. [Dockerfile Basics](#4-dockerfile-basics)
5. [Managing Docker Containers](#5-managing-docker-containers)
6. [Networking with Docker](#6-networking-with-docker)
7. [Data Management with Docker Volumes](#7-data-management-with-docker-volumes)
8. [Docker Compose](#8-docker-compose)
9. [Docker Hub and Registry](#9-docker-hub-and-registry)
10. [Docker Cleanup](#10-docker-cleanup)

## 1. Installing Docker

Install Docker on Ubuntu:

```bash
sudo apt update
sudo apt install docker.io
sudo usermod -aG docker $USER
```

Logout and login to apply group changes.

## 2. Running Your First Container

Run a simple hello-world container to test the installation:

```bash
docker run hello-world
```

## 3. Building Docker Images

Create a Dockerfile and build a custom image:

```Dockerfile
# Dockerfile
FROM ubuntu:latest
RUN apt update && apt install -y nginx
CMD ["nginx", "-g", "daemon off;"]
```

Build the image:

```bash
docker build -t my-nginx-image .
```

## 4. Dockerfile Basics

- `FROM`: Specifies the base image.
- `RUN`: Executes commands during image build.
- `CMD` or `ENTRYPOINT`: Specifies the default command to run when the container starts.

## 5. Managing Docker Containers

- `docker ps`: List running containers.
- `docker ps -a`: List all containers (including stopped ones).
- `docker stop <container_id>`: Stop a running container.
- `docker start <container_id>`: Start a stopped container.
- `docker rm <container_id>`: Remove a stopped container.

## 6. Networking with Docker

- `docker network ls`: List Docker networks.
- `docker network create <network_name>`: Create a new network.
- `docker run --network=<network_name> ...`: Connect a container to a network.

## 7. Data Management with Docker Volumes

- `docker volume ls`: List Docker volumes.
- `docker volume create <volume_name>`: Create a new volume.
- Use volumes to persist data between container restarts.

## 8. Docker Compose

Create a `docker-compose.yml` file for multi-container applications:

```yaml
version: '3'
services:
  web:
    image: nginx:latest
  db:
    image: postgres:latest
```

Run the services:

```bash
docker-compose up
```

## 9. Docker Hub and Registry

- Create a Docker Hub account: [Docker Hub](https://hub.docker.com/)
- Tag your local image: `docker tag my-nginx-image username/my-nginx-image`
- Push to Docker Hub: `docker push username/my-nginx-image`

## 10. Docker Cleanup

- `docker system prune`: Remove unused data (containers, networks, volumes, etc.).
- `docker image prune`: Remove dangling images.

---

Go back to [Docker Guide](README.md).

Visit other [Developer Guides](../README.md).
