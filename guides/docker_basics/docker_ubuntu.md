# Minimal Ubuntu Docker Image for Development Guide

This guide provides instructions for creating and using a minimal Ubuntu Docker image tailored for development purposes.

## Table of Contents

1. [Creating a Minimal Ubuntu Docker Image](#1-creating-a-minimal-ubuntu-docker-image)
2. [Dockerfile for Minimal Ubuntu Image](#2-dockerfile-for-minimal-ubuntu-image)
3. [Building and Running the Image](#3-building-and-running-the-image)
4. [Using the Development Environment](#4-using-the-development-environment)
   - [4.1. Entering a Running Container](#41-entering-a-running-container)
   - [4.2. Copying Files to Running Container](#42-copying-files-to-running-container)
   - [4.3. Attaching and Using Display](#43-attaching-and-using-display)

## 1. Creating a Minimal Ubuntu Docker Image

To create a minimal Ubuntu Docker image, use the official Ubuntu base image and minimize the installed packages. Here's a basic Dockerfile:

## 2. Dockerfile for Minimal Ubuntu Image

```Dockerfile
# Use an official minimal Ubuntu base image
FROM ubuntu:20.04

# Update package lists
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    git \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app
```

- `FROM`: Specifies the official minimal Ubuntu base image.
- `RUN`: Updates package lists, upgrades installed packages, and installs essential development tools and X11-apps for display.

## 3. Building and Running the Image

Build the Docker image from the Dockerfile:

```bash
docker build -t minimal-ubuntu-dev .
```

Run a container from the built image:

```bash
docker run -it --name minimal-ubuntu-container -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /local/folder/:/docker_workspace/folder/ minimal-ubuntu-dev
```

## 4. Using the Development Environment

Inside the container, you have a minimal Ubuntu environment with essential development tools. Customize the Dockerfile to add additional tools or packages as needed.

### 4.1. Entering a Running Container

To enter a running container:

```bash
docker exec -it minimal-ubuntu-container bash
```

### 4.2. Copying Files to Running Container

To copy files from the host machine to a running container:

```bash
docker cp /path/to/local/file minimal-ubuntu-container:/app
```

### 4.3. Attaching and Using Display

To attach and use the display with the container:

```bash
xhost +local:docker
```

This allows the container to access the X server on the host.

---

Go back to [Docker Guide](README.md).

Visit other [Developer Guides](../README.md).
