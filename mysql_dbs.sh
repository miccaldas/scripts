#!/usr/bin/zsh


mysqldump -u mic -pxxxx bkmks >> /home/mic/mysql-dbs/bkmks.sql
mysqldump -u mic -pxxxx notes >> /home/mic/mysql-dbs/notes.sql
mysqldump -u mic -pxxxx pwd >> /home/mic/mysql-dbs/pwd.sql
mysqldump -u mic -pxxxx micro_diary >> /home/mic/mysql-dbs/micro_diary.sql
