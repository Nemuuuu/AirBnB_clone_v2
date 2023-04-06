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
<html>
        <head>
                <meta charset="utf-8">
                <title>Document</title>
        </head>
        <body>
                <h1>Welcome to our Page</h1>
        </body>

</html>
" | sudo tee /data/web_static/releases/test/index.html

#create symblic link
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

#give ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

#setup nginx
sudo sed -i '/listen 80 default_server;/a \\\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t\n}' /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart
