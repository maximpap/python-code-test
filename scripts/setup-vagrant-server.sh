#!/bin/bash
USR=vagrant

apt-get update
apt-get install -y git vim build-essential python3.5-dev python3-venv \
  libncurses5-dev fabric postgresql-9.5 postgresql-server-dev-9.5 \
  libjpeg62-dev zlib1g-dev libfreetype6-dev

sudo -u postgres psql -c "CREATE DATABASE shiptrader ENCODING='UTF8' TEMPLATE=template0;"
sudo -u postgres psql -c "CREATE USER $USR;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE shiptrader TO $USR;"
sudo -u postgres psql -c "ALTER USER $USR CREATEDB;"

chmod +x /vagrant/scripts/setup-vagrant-server-user.sh
sudo -H -u $USR /vagrant/scripts/setup-vagrant-server-user.sh
