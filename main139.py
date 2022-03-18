from pyos4 import GetTid, Scheduler
from pyos5 import NewTask


def foo():
    yield NewTask(bar())


def bar():
    tid = yield GetTid()
    for _ in range(5):
        print("I'm bar", tid)
        yield


sch = Scheduler()
sch.new(foo())
sch.mainloop()
