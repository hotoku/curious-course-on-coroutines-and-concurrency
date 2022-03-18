from pyos6 import WaitTask, Scheduler, GetTid, NewTask, KillTask


def bar():
    tid = yield GetTid()
    while True:
        print("I'm bar", tid)
        yield


def main():
    tid = yield GetTid()
    print(f"main={tid}")
    child = yield NewTask(bar())
    print(f"{child=}")
    for _ in range(5):
        yield
    yield KillTask(child)


sch = Scheduler()
sch.new(main())
sch.mainloop()
