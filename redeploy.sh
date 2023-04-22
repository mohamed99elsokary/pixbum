#!/bin/bash

git push origin master
echo '
check_okay () { if [ $? != 0 ]; then echo "----- $1 -----" ; exit; fi };
echo ----------------- inside server -----------------
cd /var/www/html/pixbum/
git pull origin master
check_okay "error pulling code"
echo ----------------- done pulling code -----------------
source env/bin/activate
pip install -r requirements.txt
check_okay "error installing requirments"
echo ----------------- done updating requirements -----------------
export DJANGO_SETTINGS_MODULE=pixbum.settings.production;
python manage.py migrate
python manage.py update_translation_fields
check_okay "error migrating"
echo ----------------- done migration -----------------
sudo  supervisorctl restart pixbum
check_okay "error restarting"
echo ----------------- done restarting supervisor task -----------------
' | ssh pixbum
