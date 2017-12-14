#!/usr/bin/env bash
# this script sets up webservers for deployment of static website

sudo apt update && sudo apt install nginx -y
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "TEST CONTENT" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sfT /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i 's#location /#location /hbnb_static {\n\t\talias /data/web_static/current/\n\t}#' /etc/nginx/sites-available/default
sudo service nginx restart
