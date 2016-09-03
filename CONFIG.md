## Installation

Please see the requirements.txt for relevant python packages. Please use virtualenv to create the project.

### nuances

The parent directory of this project should also contain the following directories: "sessionfiles" and "debug".

Within the debug directory should be a "debug.txt" file. This is where print statements are redirected when running on gunicorn.

Within the sessionfiles directory should be the csv files that are used for storing the data.

### gunicorn

Perform the following commands to get gunicorn as an upstart service:

```
sudo vim /etc/init/gunicorn.conf
```

In gunicorn.conf, type the following:

```
description "Gunicorn service"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid ubuntu
setgid www-data
chdir /home/(user)/(path)/django_v1

exec /home/(user)/(path)/(Envs)/bin/gunicorn --workers 3 --bing unix:/home/(user)/(path)/django_v1/django_v1.sock django_v1.wsgi:application
```

You can now do these:

```
sudo start gunicorn
sudo stop gunicorn
sudo reload gunicorn
```

### nginx

Perform the following commands to get django to run off of the nginx server:

```
sudo vim /etc/nginx/sites-available/django_v1
```

In the file write:

```
server {

	listen 80;
	server_name (public_ip);
	
	location = /favicon.ico { access_log off; log_not_found off;}
	location /static/ {
		root /home/(user)/(path)/django_v1/(path)/static
	}

	location \ {
		include proxy_params;
		proxy_pass http://unix:/home/(user)/(path)/django_v1/django_v1.sock;
	}
}
```

Now link to sites-enabled:

```
sudo ln -s /etc/ngnix/sites-available/django_v1 /etc/ngnix/sites-enabled/django_v1
```

Now include sited-enabled to the conf file

```
sudo vim /etc/ngnix/nginx.conf
```

At the top of the http section add the following line:

```
include /etc/nginx/sites-enabled/*
```

