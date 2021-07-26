#!/usr/bin/env sh

######################################################################
# @author      : mic (mic@$HOSTNAME)
# @file        : php-xdebug
# @created     : Thursday Jul 01, 2021 22:36:31 WEST
#
# @description : Creates a file that substitutes regular PHP when
#                debugging with Vdebug and Xdebug. 
######################################################################


export XDEBUG_CONFIG="idekey=xdebug"
/usr/bin/php "$@"
