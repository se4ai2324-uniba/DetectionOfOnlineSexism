# Usa l'immagine base di Nginx
FROM nginx:latest

WORKDIR /frontend

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY . /var/www/html/

EXPOSE 80


