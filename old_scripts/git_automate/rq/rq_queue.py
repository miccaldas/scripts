"""Module Docstring"""
import subprocess
from datetime import timedelta

import isort  # noqa: F401
import snoop
from loguru import logger
from redis import Redis
from rq_scheduler import Scheduler

from git_auto import update

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def rq_queue():
    """"""
    with open("rq.txt", "w") as f:
        f.write("job in a queue")

    scheduler = Scheduler(connection=Redis())
    folders = ["/home/mic/python", "/usr/share/nginx/html/"]
    scheduler.enqueue_in(timedelta(days=1), update, folders)  # noqa: F841


@snoop
def main():
    rq_queue()


if __name__ == "__main__":
    main()
