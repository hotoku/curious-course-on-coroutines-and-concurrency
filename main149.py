from pyos6 import WaitTask, Scheduler, GetTid, NewTask, KillTask


def bar():
    tid = yield GetTid()
    for _ in range(100):
        print("I'm bar", tid)
        yield


def main():
    tid = yield GetTid()
    print(f"main={tid}")
    child = yield NewTask(bar())
    print(f"{child=}")
    yield WaitTask(child)
    print(f"child {child} finished")


sch = Scheduler()
sch.new(main())
sch.mainloop()
