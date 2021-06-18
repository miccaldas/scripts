#!/usr/bin/env zsh

 rsync  -av  --delete -e  'ssh -i /home/mic/.ssh/id_rsa' /home/mic/poems/hexo_poems/public root@45.76.37.62:/var/www/constantconstipation.club/poems/ \
 > /home/mic/cronlogs/hugo.log 2>&1
