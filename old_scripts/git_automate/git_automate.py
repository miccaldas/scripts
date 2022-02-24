"""
Automates the process of commiting, and
creating, a repository.
It's used through a daily cron job.
"""
import os
import subprocess
import sys
from datetime import datetime
from time import sleep

import isort  # noqa: F401
import snoop
from celery import Celery
from celery.utils.log import get_task_logger

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def update(path_updt, folder_name):
    """
    If there's a git repository in the folder,
    the function will run git add, commit and
    push in the directory.
    If there's not, it will create it.
    """
    os.chdir(path_updt)

    date = datetime.today().strftime("%d-%m-%Y")
    add = "git add ."
    commit = f"git commit -m '{date} commit'"
    push_github = "git push -u origin_github master"
    push_notabug = "git push -u origin master"
    cmd_notabug = f"git remote add origin git@notabug.org:micaldas/{folder_name}.git"
    cmd_init = "gh auth login --with-token < ~/documentation/github_personal_access_token"
    cmd_repo = f"gh repo create {folder_name} --disable-issues --disable-wiki --public --remote=origin_github --source=. --push"
    cmd_create = "git init -b master"
    cmd_ignore = "git-ignore python"
    cmd_add = "git add ."
    cmd_commit = "git commit -m 'First Commit'"

    with open(f"{path_updt}/.git/config", "r") as f:
        git_remotes = f.readlines()
        gr = str(git_remotes)
        if '[remote "origin"]' in gr:
            subprocess.run(add, cwd=path_updt, shell=True)
            sleep(1)
            subprocess.run(commit, cwd=path_updt, shell=True)
            sleep(1)
            subprocess.run(push_notabug, cwd=path_updt, shell=True)
            sleep(1)
        else:
            subprocess.run(cmd_notabug, cwd=path_updt, shell=True)
        if '[remote "origin_github"]' in gr:
            subprocess.run(add, cwd=path_updt, shell=True)
            sleep(1)
            subprocess.run(commit, cwd=path_updt, shell=True)
            sleep(1)
            subprocess.run(push_github, cwd=path_updt, shell=True)
        else:
            subprocess.run(cmd_create, cwd=path_updt, shell=True)
            sleep(2)
            subprocess.run(cmd_ignore, cwd=path_updt, shell=True)
            sleep(2)
            subprocess.run(cmd_add, cwd=path_updt, shell=True)
            sleep(2)
            subprocess.run(cmd_commit, cwd=path_updt, shell=True)
            sleep(2)
            subprocess.run(cmd_init, cwd=path_updt, shell=True)
            sleep(2)
            subprocess.run(cmd_repo, cwd=path_updt, shell=True)


app = Celery("end", broker="redis://localhost:6379/0")


@app.task(name="git_automate.end", bind=True)
def end(number):

    print(number)
    print(sys.argv)
    logger = get_task_logger(__name__)
    app.config_from_object("celeryconfig")
    folders = ["/home/mic/python", "/usr/share/nginx/html/"]
    for folder_name in folders:
        logger.info("folder_name - {0}".format(folder_name))
        for path_updt in os.listdir(folder_name):
            logger.info("path_updt - {0}".format(path_updt))
            res = update.delay(path_updt, folder_name)
            print(res.state)
            print(res.successful)
            print(res.get())


if __name__ == "main":
    end()
