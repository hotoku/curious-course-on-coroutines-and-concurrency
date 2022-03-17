def grep(pattern):
    print("Looking for %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line, end="")
