from pyos8 import *
from socket import socket, AF_INET, SOCK_STREAM


def handle_client(client, addr):
    print("Connection from", addr)
    while True:
        data = yield Recv(client, 65536)
        if not data:
            break
        yield Send(client, data)
    print("Client closed")
    client.close()


def server(port):
    print("Server starting")
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(5)
    while True:
        client, addr = yield Accept(sock)
        yield NewTask(handle_client(client, addr))


def alive():
    while True:
        print("I'm alive!")
        yield


sched = Scheduler()
# sched.new(alive())
sched.new(server(45000))
sched.mainloop()
