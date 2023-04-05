#!/usr/bin/env bash
# script to setup web servers for the deployment of web static

#install nginx
sudo apt-get update -y
sudo apt-get install nginx -y

#create folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#create html file with fake content
echo "
<!DOCTYPE html>
<html lang="en">
        <head>
                <meta charset="utf-8">
                <title>Document</title>
        </head>
        <body>
                <h1>Welcome to our Page</h1>
        </body>

</html>
"  > sudo /data/web_static/releases/test/index.html

#create symblic link
sudo rm /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#give ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

#setup nginx
sudo sed -i '/listen 80 default_server/a location /hbnb_static {
                alias /data/web_static/current;
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a >
                try_files $uri $uri/ =404;
        }' /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart
