from pyos8 import *
from socket import socket, AF_INET, SOCK_STREAM

from sockwrap import Socket


def handle_client(client, addr):
    print("Connection from", addr)
    while True:
        data = yield client.recv(65536)
        if not data:
            break
        yield client.send(data)
    print("Client closed")
    yield client.close()


def server(port):
    print("Server starting")
    rawsock = socket(AF_INET, SOCK_STREAM)
    rawsock.bind(("", port))
    rawsock.listen(5)
    sock = Socket(rawsock)
    while True:
        client, addr = yield sock.accept()
        yield NewTask(handle_client(client, addr))


def alive():
    while True:
        print("I'm alive!")
        yield


sched = Scheduler()
# sched.new(alive())
sched.new(server(45000))
sched.mainloop()
