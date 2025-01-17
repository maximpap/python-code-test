#!/bin/bash
# VirtualEnv and Django setup

USR=vagrant

# Set up virtualenv directory for the user if required
if [ ! -d /home/$USR/.virtualenvs ]; then
    mkdir /home/$USR/.virtualenvs
fi

# write all the profile stuff for the user if required
grep -q virtualenvs /home/$USR/.bashrc
if [ $? -ne 0 ]; then
    echo -e "\033[0;31m > Updating profile file\033[0m"
    echo "source ~/.virtualenvs/code-test/bin/activate" >> /home/$USR/.bashrc
    echo "cd /vagrant/" >> /home/$USR/.bashrc
    echo "alias runserver='/vagrant/manage.py runserver 0:8008'" >> /home/$USR/.bashrc
fi

echo -e "\033[0;34m > Setting up virtualenv\033[0m"
export WORKON_HOME=/home/$USR/.virtualenvs
export PIP_VIRTUALENV_BASE=/home/$USR/.virtualenvs
python3 -m venv $PIP_VIRTUALENV_BASE/code-test
source $PIP_VIRTUALENV_BASE/code-test/bin/activate

# install requirements
echo -e "\033[0;34m > Installing the pip requirements.\033[0m"
$PIP_VIRTUALENV_BASE/code-test/bin/pip install -U pip
$PIP_VIRTUALENV_BASE/code-test/bin/pip install wheel==0.29.0
$PIP_VIRTUALENV_BASE/code-test/bin/pip install -r /vagrant/requirements.in

# setup db state
cd /vagrant
./manage.py migrate
