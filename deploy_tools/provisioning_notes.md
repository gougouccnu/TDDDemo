Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com  or 191.101.226.187

## Upstart Job not ok for me lsw

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

instead of gunicorn manully

* ../virtual/bin/gunicorn --bind unix:/tmp/SITENAME.socket superlists.wsgi:application
* replace SITENAME with, eg 191.101.226.187 
## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv
