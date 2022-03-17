from timeit import timeit

from coroutine import coroutine


@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


class GrepHandler:
    def __init__(self, pattern, target):
        self.target = target
        self.pattern = pattern

    def handle(self, line):
        if self.pattern in line:
            self.target.send(line)


@coroutine
def null():
    while True:
        _ = (yield)


line = "python is nice"
p1 = grep("python", null())
p2 = grep("python", null())


f1 = timeit("p1.send(line)", "from __main__ import line, p1", number=10**7)
f2 = timeit("p2.send(line)", "from __main__ import line, p2", number=10**7)
print(f1, f2)
