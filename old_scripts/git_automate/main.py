"""Module Docstring"""
import os

from git_automate import end

pid = os.getpid()
print(pid)
with end.delay(1) as result:
    print(result)
    print(result.ready())
    print(result.get())
    print(end.name)
