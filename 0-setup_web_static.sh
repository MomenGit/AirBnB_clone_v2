#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "<html>
  <head>
  </head>
  <body>
    ALX School
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/server_name _;/a \
    #\n\tlocation /hbnb_static/ {\
        \n\t\talias /data/web_static/current/;\
    \n\t}" /etc/nginx/sites-enabled/default

sudo service nginx restart
