from pyos4 import GetTid, Scheduler


def foo():
    tid = yield GetTid()
    for _ in range(10):
        print("I'm foo", tid)
        yield


def bar():
    tid = yield GetTid()
    for _ in range(5):
        print("I'm bar", tid)
        yield


sch = Scheduler()
sch.new(foo())
sch.new(bar())
sch.mainloop()
