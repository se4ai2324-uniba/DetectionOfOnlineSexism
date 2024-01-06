# Docker

Docker is a lightweight virtualization tool that allows us to isolate the development environment and ensure the reproducibility of our experiments.

## Components

- [Dockerfile](../../Dockerfile): The Dockerfile contains instructions for creating the Docker image. This file defines the environment and dependencies required to run our machine learning project.

- [docker-compose.yml](../../docker-compose.yml): The docker-compose.yml file is used to configure the Docker service so that we can quickly start our development environment. It contains configurations for Docker services, volumes, and networks.

- [requirements.txt](../../requirements.txt): This file lists all the Python dependencies required for our machine learning project. These dependencies will be installed when the Docker image is created.

- [data/](../../data): This folder should contain all the training and test data required for the machine learning project. Make sure the data is accessible within the Docker container.

- [src/](../../src): In this folder, you may want to place our development scripts that we will use during the project. These can be mounted inside the Docker container for execution and editing.

## Usage

To use this Docker environment for our machine learning project, follow these steps:

1. Make sure you have Docker installed on your system.

2. Navigate to the directory containing these files.

3. Build the Docker images by running the following commands, which define the realtive images at the backend and the frontend respectively:

```bash
docker build -t detectionofonlinesexism_backend .
```
```bash
docker build -t detectionofonlinesexism_frontend ./frontend
```

These commands will create the Docker images based on their Dockerfile and with the dependencies specified in `requirements.txt`.

4. Start the Docker container using docker-compose:
```bash
docker-compose up
```

This command activates the container based on the docker-compose.yml configuration. Alternatively, you can build and start the container in one step:
```bash
docker-compose up --build  
```
Once running, you can access the Docker development environment.

5. Access the Docker development environment and begin working on our machine learning projects. In our case, we can se the following dashboard:

![Docker Dashboard](../images_doc/DockerDashboard.png)

6. When you're done, you can stop the Docker container with the following command:

```bash
docker-compose down
```

