from coroutine import coroutine


@coroutine
def grep(pattern):
    print("Looking for %s" % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("bye")


g = grep("python")
for l in ["a", "b", "c", "python"]:
    g.send(l)
g.close()
