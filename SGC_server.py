#!/usr/bin/env python
from socket import *
from addresses import db

HOST = '127.0.0.1'
PORT = 29877
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket( AF_INET,SOCK_STREAM)
serv.bind((ADDR))
serv.listen(1)

d = []
inp = None


while True:
    print "Listening"

    conn, addr = serv.accept()

    print "Connected to ", ADDR
    conn.send("Welcome to StarGate Command ")

    while True:

        # 6 symbols
        if len(d) == 6:
            break

        # store the users input
        inp = conn.recv(BUFSIZE)
        d.append(int(inp))

    # compare the users list with the lists in the address database
    for k, v in db.iteritems():
        if cmp(d, v) == 0:
            conn.send('%s MATCH - %s' % (k, d))


conn.close()
