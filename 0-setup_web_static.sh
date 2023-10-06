#!/usr/bin/env bash
# script to setup server for deployment of web_static

sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo ln -f -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "Sample text" > /data/web_static/releases/test/index.html
sudo chown ubuntu:ubuntu /data/web_static/releases/test/index.html
sudo chown -R ubuntu:ubuntu /etc/nginx/sites-available/default
sudo sed -i 's#root /var/www/html;#root /var/www/html;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}#1' /etc/nginx/sites-available/default
sudo service nginx restart
