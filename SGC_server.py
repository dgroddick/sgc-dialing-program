#!/usr/bin/env python
from socket import *
from addresses import db

NUM_CHEVRONS = 6

user_data = []  # list for storing the whole address the users sends
inp = None

HOST = '127.0.0.1'
PORT = 29877
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket( AF_INET,SOCK_STREAM)
serv.bind((ADDR))
serv.listen(1)

# listen loop
while True:

    conn, addr = serv.accept()

    conn.send("Welcome to StarGate Command ")

    # collect user input
    while True:

        # 6 symbols plus point of origin
        if len(user_data) == NUM_CHEVRONS:
            break

        # store the users input into the list
        inp = conn.recv(BUFSIZE)
        user_data.append(int(inp))

    # compare the users list with the lists in the address database
    for key, value in db.iteritems():
        if cmp(user_data, value) == 0:
            conn.send('%s - ENCODED .... Connecting to:  %s' % (user_data, key))


conn.close()
