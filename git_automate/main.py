"""
Automates the process of commiting, and
creating, a repository.
It's used through a daily cron job.
"""
import os
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

from git_automate import update

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/spam.log", level="DEBUG", format=fmt, backtrace=True, diagnose=True)
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def main():
    """
    Checks if folders in the python and site folders have a repo,
    if not it creates it, if they're already have one, it runs a
    update, by turning the git commannds in variables and running
    in sequence over each one of the sources.
    """

    folders = ["/home/mic/python/", "/usr/share/nginx/html/"]

    for folder in folders:
        os.chdir(folder)
        paths = []
        for f in os.listdir(folder):
            jn = folder + f
            if os.path.isdir(jn):
                paths.append(jn)
        for path in paths:
            path_updt = path
            folder_name = os.path.basename(os.path.normpath(path_updt))
            update(path_updt, folder_name)


if __name__ == "__main__":
    main()
