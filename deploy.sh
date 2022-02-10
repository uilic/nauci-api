#!/bin/sh
sudo git pull origin main
sudo pip3 install -r requirements.txt
sudo mkdir testdir
sudo systemctl restart gunicorn
sudo systemctl restart nginx
