from pyos7 import *
from socket import *


def handle_client(client, addr):
    print("Connection from", addr)
    while True:
        yield ReadWait(client)
        data = client.recv(65536)
        print(data.decode("utf-8"))
        if not data:
            break
        yield WriteWait(client)
        client.send(data)
    client.close()
    print("Client closed")
    yield


def server(port):
    print("Server starting")
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(5)
    while True:
        yield ReadWait(sock)
        client, addr = sock.accept()
        yield NewTask(handle_client(client, addr))


def alive():
    while True:
        print("I'm alive!")
        yield


sched = Scheduler()
# sched.new(alive())
sched.new(server(45000))
sched.mainloop()
