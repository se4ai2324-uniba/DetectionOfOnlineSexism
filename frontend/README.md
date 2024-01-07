# Frontend with Nginx

This directory contains the frontend part of our application, implemented using Nginx as a web server. It includes all necessary HTML, CSS, JavaScript files, and a logo. The setup is designed to be run in a Docker container for easy deployment and scalability.

## Structure

- HTML, CSS, JS Files: The core files for the frontend UI.
- [nginx.conf](./nginx.conf) : Nginx configuration file to manage server requests and proxy settings.
- [Dockerfile](./Dockerfile) : Instructions for building the frontend Docker image with Nginx.

## Nginx Configuration

The `nginx.conf` file is set up to:

- Serve static files (HTML, CSS, JS) from `/var/www/html`.
- Proxy requests to `/api/prediction_category` and `/api/prediction_sexism` to the backend service.

## Dockerfile

The Dockerfile uses the latest Nginx image, sets the working directory, copies the Nginx configuration, and all frontend files into the image, and exposes port 80.

## Usage

### Building and Running with Docker

1. **Build the Docker Image**:
Navigate to the frontend directory and build the Docker image:
```bash
docker build -t detectionofonlinesexism_frontend ./frontend
```

2. **Run the Docker Container**:
Start a container from the image:
```bash
docker run -d -p 80:80 detectionofonlinesexism_frontend
```
This will start the Nginx server and serve the frontend on port 80 of your host machine.

3. **Accessing the Frontend**
After starting the Docker container, the frontend will be accessible via http://localhost or your server's IP address/domain.

### Proxy Configuration

The Nginx server proxies certain API requests to the backend service:

* **Prediction Category API**: Requests to /api/prediction_category are proxied to http://backend:8000/prediction_category.
* **Prediction Sexism API**: Requests to /api/prediction_sexism are proxied to http://backend:8000/prediction_sexism.

Ensure that the backend service is accessible at the specified URL and port for these proxies to function correctly.