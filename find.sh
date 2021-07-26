#!/usr/bin/env sh

######################################################################
# @author      : mic (mic@$HOSTNAME)
# @file        : find
# @created     : Thursday Jun 24, 2021 02:45:40 WEST
#
# @description : Use gnu find with some folders excluded 
######################################################################

echo Search? 
read varname
exec sudo find / -name $varname ! -path "/mnt/*" ! -path "/var/lib/docker/*"
