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
