#!/usr/bin/env python
from socket import *
from addresses import db

NUM_CHEVRONS = 6
POINT_OF_ORIGIN = 1

dialed_address = []  # list for storing the whole address the users sends
inp = None

HOST = '127.0.0.1'
PORT = 29876
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket(AF_INET,SOCK_STREAM)
serv.bind((ADDR))
serv.listen(1)

listen = True

# listen loop
while listen:

    conn, addr = serv.accept()
    print "Connected to client %s\n" % (str(addr))

    conn.send("Welcome to StarGate Command \n\n")

    # collect user input
    while True:

        # 6 symbols plus point of origin
        if len(dialed_address) == NUM_CHEVRONS:
            break
        else:
            # store the users input into the list
            inp = conn.recv(BUFSIZE)
            dialed_address.append(int(inp))
            print "%d ENCODED" % (int(inp))
            conn.send("ENCODED\n")

    # compare the users list with the lists in the address database
    for key, value in db.iteritems():
        if cmp(dialed_address, value) == 0:
            print "%s - WORMHOLE ESTABLISHED" % (dialed_address)
            print "\n .... Connecting to:  %s\n" % (key)

            conn.send("%s - WORMHOLE ESTABLISHED" % (dialed_address))
            conn.send("\n .... Connecting to:  %s\n" % (key))
            listen = False


conn.close()
