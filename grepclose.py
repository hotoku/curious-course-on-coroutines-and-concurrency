from coroutine import coroutine


@coroutine
def grep(pattern):
    print("Looking for %s" % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line, end="")
    except GeneratorExit:
        print("bye")
