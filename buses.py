from coroutine import coroutine


@coroutine
def buses_to_dicts(target):
    while True:
        event, value = (yield)
        if event == "start" and value[0] == "buses":
            while True:
                event, value = (yield)
                if event == "start" and value[0] == "bus":
                    ret = {}
                    while True:
                        event, value = (yield)
                        if event == "start":
                            key = value[0]
                            ret[key] = ""
                            while True:
                                event, value = (yield)
                                if event == "end":
                                    break
                                elif event == "characters":
                                    ret[key] += value
                        elif event == "end":
                            break
                    target.send(ret)


@coroutine
def filter_on_filed(field, value, target):
    while True:
        bus = (yield)
        if bus.get(field) == value:
            target.send(bus)


@coroutine
def location():
    while True:
        bus = (yield)
        print("%(id)s, %(route)s" % bus)
