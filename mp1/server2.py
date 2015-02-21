#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5002
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)


#this will do the listening part and print incoming messagaes
while 1:
	conn, addr = s.accept()
	data = conn.recv(BUFFER_SIZE)
	if data:
		print "received data:", data
conn.close()

