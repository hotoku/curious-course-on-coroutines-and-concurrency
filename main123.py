from pyos2 import Scheduler


def foo():
    for _ in range(10):
        print("I'm foo")
        yield


def bar():
    while True:
        print("I'm bar")
        yield


sch = Scheduler()
sch.new(foo())
sch.new(bar())
sch.mainloop()
