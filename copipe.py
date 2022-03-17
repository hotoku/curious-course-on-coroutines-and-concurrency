from cofollow import printer
from cofollow import follow
from coroutine import coroutine


@coroutine
def grep(pattern, target):
    print("Looking for %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


fp = open("access-log")
follow(fp, grep("python", printer()))
