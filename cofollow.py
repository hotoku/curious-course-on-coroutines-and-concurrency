from coroutine import coroutine
import time
from typing import TextIO


@coroutine
def follow(thefile: TextIO, target):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


@coroutine
def printer():
    while True:
        line = (yield)
        print(line, end="")
