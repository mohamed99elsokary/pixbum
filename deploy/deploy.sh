#!/bin/bash
DIRECTORY=$(cd $(dirname $0) && pwd)

cd ..
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

cd deploy

sudo ln -s $DIRECTORY/pixbum.supervisor.conf /etc/supervisor/conf.d/pixbum.supervisor.conf
sudo supervisorctl reread
# sudo supervisorctl reload
sudo supervisorctl restart pixbum
echo "enter any key to continue."
read
sudo ln -s $DIRECTORY/pixbum.nginx.conf /etc/nginx/sites-available/

sudo ln -s $DIRECTORY/pixbum.nginx.conf /etc/nginx/sites-available/pixbum.nginx.conf
sudo ln -s /etc/nginx/sites-available/pixbum.nginx.conf /etc/nginx/sites-enabled/pixbum.nginx.conf
sudo nginx -t
echo "enter any key to continue with restarting nginx"
read
sudo service nginx restart
