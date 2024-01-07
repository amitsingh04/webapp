
## Python Install and Virtual Environment
```bash
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt install python3-venv
```
Create virtual environment
```bash
python3 -m venv venv
```
Install required packages 
```bash
pip install -r requirements.txt
```
Note the requirement file is in the project.


## Apache Configuration on ubuntu or debian
### Apache and mod wsgi Installation

```bash
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3
```
### Source Code location
Clone and copy the location to directory /var/www.
### create webapp.conf at location /etc/apache2/sites-available
```xml
<VirtualHost *:80>
               ServerName <serverfqdn>
               ServerAdmin <email>
               WSGIScriptAlias / /var/www/webapp/webapp.wsgi
               <Directory /var/www/webapp/>
                       Order allow,deny
                       Allow from all
               </Directory>
               Alias /static /var/www/webapp/static
               <Directory /var/www/webapp/static/>
                       Order allow,deny
                       Allow from all
               </Directory>
               ErrorLog ${APACHE_LOG_DIR}/webapp_error.log
               LogLevel warn
               CustomLog ${APACHE_LOG_DIR}/webapp_access.log combined
</VirtualHost>
```
If using virtual environment modify the /etc/apache2/mods-available/wsgi.conf value for WSGIPythonPath

WSGIPythonPath /var/www/webapp:/var/www/webapp/venv:/var/www/webapp/venv/lib/python3.10/site-packages

Note: In this case I'm using python version 3.10 but it can be different in your case.
