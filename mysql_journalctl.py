from mysql.connector import connect, Error
import subprocess
from loguru import logger

################################################################################
# @author      : mclds
# @file        : mysql_journalctl
# @created     : 12/08/2021
# @email       : mclds@protonmail.com
# @description : Journalctl view of mariadb during the last 5 minutes.
#
################################################################################

fmt = "{time} - {name} - {level} - {message}"
logger.add("spam.log", level="DEBUG", format=fmt, backtrace=True, diagnose=True)
logger.add("error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


@logger.catch  # Decorator for loguru. All errors will go log. Has to be on all functions
def journalctl():
    cmd = 'sudo journalctl -u mariadb --since "5 minutes ago"'
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    journalctl()
