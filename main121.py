from pyos2 import Scheduler


def foo():
    while True:
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
