from pyos6 import WaitTask, Scheduler, GetTid, NewTask


def bar():
    tid = yield GetTid()
    for _ in range(5):
        print("I'm bar", tid)
        yield


def main():
    myid = yield GetTid()
    print(myid)
    child = yield NewTask(bar())
    print(child)


sch = Scheduler()
sch.new(main())
sch.mainloop()
