#!/usr/bin/env zsh
# -*- coding: utf-8 -*-

######################################################################
# Author           : mic
# File             : snippets
# Date Created     : Monday Apr 19, 2021 01:35:10 WEST
# @description     : Deletes outtput, regenrates content, sends it to
# sickly where it's hosted. Made in Pelican
######################################################################


sudo rm -r /home/mic/web_projects/snippets_blog/output
cd /home/mic/web_projects/snippets_blog
make html
sudo rsync  -av  --delete -e  'ssh -i /home/mic/.ssh/id_rsa' /home/mic/web_projects/snippets_blog/output root@140.82.58.233:/var/www/html > /home/mic/cronlogs/snippets.log 2>&1
