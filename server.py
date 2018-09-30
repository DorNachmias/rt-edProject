#!/usr/bin/python
import socket
import sqlite3
import time

#Updating DataBase
def dbs(x):
    '''
    Organize text and saves to DB
    :param x:
    :return void:
    '''
    #Convert to String and edit
    x=x.decode()
    x.replace("b'", "")
    x.replace("'", "")
    task=x.split()
    task[1]=task[1]+" "+task[2]
    del task[2]
    #SQL DataBase Insert and Save
    db = sqlite3.connect("data.db")
    sql = '''INSERT INTO DATA (id,time,alarm1,alarm2)
            VALUES (?,?,?,?)
                '''
    cursor=db.cursor()
    print("Updating DB", x)
    cursor.execute(sql, task)
    db.commit()
    db.close()


#Socket prep work

serv=socket.socket()
serv.bind(("",5001))
serv.listen(3)

#Establishing Connections

while True:
    client, addr = serv.accept()
    print("Connected to ",addr)
    client.send(b"keep alive")
    x=client.recv(2048)
    dbs(x)
    x=x.decode()
    x=x.split()
    time.sleep(60)
