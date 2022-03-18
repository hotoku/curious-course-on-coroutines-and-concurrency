from pyos3 import Scheduler


def foo():
    for _ in range(10):
        print("I'm foo")
        yield


def bar():
    for _ in range(5):
        print("I'm bar")
        yield


sch = Scheduler()
sch.new(foo())
sch.new(bar())
sch.mainloop()
