#!/usr/bin/env sh

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : strace_translated
# @created     : Friday Nov 12, 2021 19:35:05 WET
#
# @description : Turns strace output more understandable.
# @source      : https://tinyurl.com/yfp8sysy
######################################################################

echo What command do you want to strace?
read -p 'Search: ' pergunta

strace -f -e trace=read,write,recvfrom,sendto -s 1000 -f $pergunta 2>&1 | grep --line-buffered -o '".\+[^"]"' | grep --line-buffered -o '[^"]*[^"]' | while read -r line; do printf "%b" $line; done | tr "\r\n" "\275\276" | tr -d "[:cntrl:]" | tr "\275\276" "\r\n" 
