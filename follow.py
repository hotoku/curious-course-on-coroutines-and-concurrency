import time
from typing import TextIO


def follow(thefile: TextIO):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


logfile = open("access-log")
for line in follow(logfile):
    print(line, end="")
