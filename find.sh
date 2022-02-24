#!/usr/bin/env sh

######################################################################
# @author      : mic (mic@$HOSTNAME)
# @file        : find
# @created     : Thursday Jun 24, 2021 02:45:40 WEST
#
# @description : Use gnu find with some folders excluded 
######################################################################

exec sudo find / -name $1 ! -path "/home/mic/secondary-hard-drive/*"
