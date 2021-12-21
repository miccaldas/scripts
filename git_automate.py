import subprocess
import time
from datetime import datetime
import snoop
from loguru import logger

################################################################################
# @author      : mclds
# @file        : mysql_journalctl
# @created     : 12/08/2021
# @email       : mclds@protonmail.com
# @description : Automates the process of commiting to a repository. It's used
#                through a daily cron job.
################################################################################

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/spam.log", level="DEBUG", format=fmt, backtrace=True, diagnose=True)
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


@snoop
def git():
    """Turned the git commannds in variables and made them run in sequence
    over each one of the sources."""

    date = datetime.today().strftime("%d-%m-%Y")
    add = "git add ."
    commit = f"git commit -m '{date} commit'"
    push_codeberg = "git push -u origin_codeberg master"
    push_notabug = "git push -u origin master"

    paths = [
        "/home/mic/python/bkmk",
        "/home/mic/python/books",
        "/home/mic/python/cli_app_list",
        "/home/mic/python/encrypt_diary",
        "/home/mic/python/html_project",
        "/home/mic/python/logging_functions",
        "/home/mic/python/micro_diary",
        "/home/mic/python/notes",
        "/home/mic/python/old_alternative_projects",
        "/home/mic/python/player",
        "/home/mic/python/pwd",
        "/home/mic/python/python_project",
        "/home/mic/python/rss",
        "/home/mic/python/scraper",
        "/home/mic/python/todos",
        "/home/mic/python/tree",
        "/home/mic/python/urlshort",
        "/home/mic/server_html_projects",
        "/home/mic/scripts",
    ]

    for path in paths:
        subprocess.run(add, cwd=path, shell=True)
        time.sleep(1)
        subprocess.run(commit, cwd=path, shell=True)
        time.sleep(1)
        subprocess.run(push_codeberg, cwd=path, shell=True)
        time.sleep(1)
        subprocess.run(push_notabug, cwd=path, shell=True)
        time.sleep(1)


if __name__ == "__main__":
    git()
