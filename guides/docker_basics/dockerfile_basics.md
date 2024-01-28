# Dockerfile Basics Guide

This guide provides a quick reference for creating Dockerfiles, which are used to define the configuration and dependencies for building Docker images.

## Table of Contents

1. [Understanding Dockerfile](#1-understanding-dockerfile)
2. [Basic Structure](#2-basic-structure)
3. [Common Instructions](#3-common-instructions)
4. [Building and Running Docker Image](#4-building-and-running-docker-image)
5. [Best Practices](#5-best-practices)

## 1. Understanding Dockerfile

A Dockerfile is a text document containing a set of instructions that Docker uses to create a Docker image. It defines the base image, sets up the environment, and specifies the commands to run within the container.

## 2. Basic Structure

A simple Dockerfile typically consists of the following elements:

```Dockerfile
# Use an official base image
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Copy application files into the container
COPY . .

# Install dependencies
RUN apt-get update && apt-get install -y python3

# Define the default command to run when the container starts
CMD ["python3", "app.py"]
```

- `FROM`: Specifies the base image.
- `WORKDIR`: Sets the working directory inside the container.
- `COPY`: Copies files from the local machine to the container.
- `RUN`: Executes commands during image build.
- `CMD` or `ENTRYPOINT`: Specifies the default command to run when the container starts.

## 3. Common Instructions

### 3.1. **FROM**

```Dockerfile
FROM ubuntu:latest
```

Specifies the base image for the Docker image.

### 3.2. **WORKDIR**

```Dockerfile
WORKDIR /app
```

Sets the working directory inside the container.

### 3.3. **COPY**

```Dockerfile
COPY . .
```

Copies files from the local machine to the container.

### 3.4. **RUN**

```Dockerfile
RUN apt-get update && apt-get install -y python3
```

Executes commands during image build.

### 3.5. **CMD** or **ENTRYPOINT**

```Dockerfile
CMD ["python3", "app.py"]
```

Specifies the default command to run when the container starts.

## 4. Building and Running Docker Image

Build the Docker image from the Dockerfile:

```bash
docker build -t my-app-image .
```

Run a container from the built image:

```bash
docker run my-app-image
```

## 5. Best Practices

- Keep images small by using a minimal base image.
- Combine commands to minimize layers.
- Leverage caching for efficiency.
- Avoid installing unnecessary dependencies.
- Use a `.dockerignore` file to exclude unnecessary files during the build.

---

Go back to [Docker Guide](README.md).

Visit other [Developer Guides](../README.md).
