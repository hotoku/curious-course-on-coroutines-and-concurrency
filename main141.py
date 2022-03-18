from pyos4 import GetTid, Scheduler
from pyos5 import KillTask, NewTask


def main():
    tid = yield NewTask(bar())
    for _ in range(5):
        yield
    yield KillTask(tid)


def bar():
    tid = yield GetTid()
    while True:
        print("I'm bar", tid)
        yield


sch = Scheduler()
sch.new(main())
sch.mainloop()
