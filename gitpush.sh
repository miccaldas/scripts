#!/usr/bin/env python3.9
""" Automation of the git process of adding, commiting and pushing data """
import subprocess


def push():
    """ Subprocess is run with shell=True, so as to function exactly like in the shell """
    title = input('Choose a title for the commit ')
    subprocess.run(['git add .'], shell=True)
    subprocess.run(['git commit -m ' + title], shell=True)
    subprocess.run(['git push origin master'], shell=True)
    subprocess.run(['git push origin_gogs master'], shell=True)


if __name__ == '__main__':
    push()
