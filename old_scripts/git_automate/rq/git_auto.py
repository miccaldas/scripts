"""
Automates the process of commiting, and
creating, a repository.
It's used through a daily cron job.
"""
import os
import subprocess
from datetime import datetime
from time import sleep

import isort  # noqa: F401
import snoop

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def update(folders):
    """
    If there's a git repository in the folder,
    the function will run git add, commit and
    push in the directory.
    If there's not, it will create it.
    """
    for folder in folders:
        fullpaths = [os.path.join(folder, file) for file in os.listdir(folder)]
    for full in fullpaths:
        path_updt = full
    folder_name = folder

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


if __name__ == "__main__":
    update()
