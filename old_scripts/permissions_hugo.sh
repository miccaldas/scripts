#!/usr/bin/env python

from fabric import Connection

c = Connection(
    host = 'constantconstipation.club',
    user = 'root',
    connect_kwargs={
        'key_filename': '/home/mic/.ssh/id_rsa'
    }
)

c.run('cd /var/www/constantconstipation.club/html/ && chown -R www-data:www-data public')