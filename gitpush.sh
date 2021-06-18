#!/usr/bin/env zsh

######################################################################
# @author      : mic (mic@$HOSTNAME)
# @file        : gitpush
# @created     : Friday Jun 18, 2021 08:30:18 WEST
#
# @description : Automate pushing to git repo 
######################################################################


git add .

echo 'Enter the commit message:'
read commitMessage

git commit -m "$commitMessage"

echo 'Enter the name of the remote:'
read remote

git push $remote main

read
