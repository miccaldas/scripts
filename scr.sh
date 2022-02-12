#!/bin/bash


######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : scr
# @created     : Saturday Feb 05, 2022 21:33:37 UTC
#
# @description : Not really sure what it does but it is supposed to
# help you retrieve files that you may have deleted in error.
######################################################################


if [[ ! $1 ]]; then
    echo -e "Usage:\n\n\t$0 'i_string.txt'"
    exit 1
fi

f=$(file 2>/dev/null /proc/*/fd/* | awk '$NF == "(deleted)"{print $(NF-1)}')

if [[ $f ]]; then
    echo "fd $f found..."
    cp -v "$f" "$1"
else
    echo >&2 "No fd found..."
    exit 2
fi
