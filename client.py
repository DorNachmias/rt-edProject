#!/usr/bin/python3

import socket
import datetime
from uuid import getnode as get_mac

while True:
    #Socket prep
    c = socket.socket()
    c.connect(("127.0.0.1",5001))

    #order
    order=c.recv(1024)

    if order==(b"keep alive"):
        #Gathering data for report
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        f=open("status.txt", 'r')
        cont=f.readlines()
        f.close()
        #Self ID check (MAC or given)
        if cont[0][0] == '#':
            id = get_mac()
        else:
            id = cont[0]
            id = id.replace("\n", "")
        #Actual transmission
        c.send((str(id)+" "+now+" "+cont[2]).encode())
    c.close()