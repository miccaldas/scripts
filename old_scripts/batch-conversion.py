#!/usr/bin/env python

######################################################################
# @author      : mic (mic@$HOSTNAME)
# @file        : batch-conversion
# @created     : Saturday Jun 26, 2021 03:52:05 WEST
#
# @description : Convert all .md files in a directory into HTML.
######################################################################
import subprocess


def batch_conversion():
    """ We will open the file with the names of the files and use a command line \
    command to make the conversion."""

    f = open("list.txt", "r")
    md = f.readline()
    while md:
        subprocess.run(['python -m markdown ' + md.strip() + ' -f ' + md.strip() + '.html'], shell=True)
        # .strip are there so Python won't read line with the line break symbol attached
        md = f.readline()
    f.close()


if __name__ == '__main__':
    batch_conversion()
