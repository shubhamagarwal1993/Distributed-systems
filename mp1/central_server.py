#!/usr/bin/env python

import socket
import sys
import thread
import threading
import time
import readline
import io
import random
import re
import datetime

f=open('config0.txt')
lines=f.readlines()

TCP_IP = lines[1].rstrip('\n')
TCP_PORT = lines[2]
BUFFER_SIZE = lines[5]
aString = 'i am central server'
my_server_id = 0

Server_TCP_IP = '127.0.0.1'

#Max delay time in seconds
MAX = lines[24]
firstWord = 'a'
secondWord = 'a'
thirdWord = 1
Key = 1
Model = 0
Value = 1
ack = 0

q = []				#this queue maintains bcast msg from servers

def q1_thread():
	wait_time = random.randint(0, int(MAX))
	global ack
	time.sleep(int(wait_time))
	try:
		s11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print q
		msg_to_send = q[0][0]
		msg_to_send = ' ' + msg_to_send
		msg_to_send = "central_server" + msg_to_send  
		s11.connect((Server_TCP_IP, 5001))
		s11.send(msg_to_send)
		ttt = s11.recv(5)
		s11.close()
	except socket.error,msg:
		pass
	ack += 1

def q2_thread():
	wait_time = random.randint(0, int(MAX))
	global ack
	time.sleep(int(wait_time))
	try:
		s12 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		msg_to_send = q[0][0]
		msg_to_send = ' ' + msg_to_send
		msg_to_send = "central_server" + msg_to_send
		s12.connect((Server_TCP_IP, 5002))
		s12.send(msg_to_send)
		drs12.recv(1024)
		s12.close()
	except socket.error,msg:
		pass
	ack += 1

def q3_thread():
	wait_time = random.randint(0, int(MAX))
	global ack
	time.sleep(int(wait_time))
	try:
		s13 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		msg_to_send = q[0][0]
		msg_to_send = ' ' + msg_to_send
		msg_to_send = "central_server" + msg_to_send 
		s13.connect((Server_TCP_IP, 5003))
		s13.send(msg_to_send)
		s13.recv(1024)
		s13.close()
	except socket.error,msg:
		pass
	ack += 1

def q4_thread():	
	wait_time = random.randint(0, int(MAX))
	global ack
	time.sleep(int(wait_time))
	try:
		s14 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		msg_to_send = q[0][0]
		msg_to_send = ' ' + msg_to_send
		msg_to_send = "central_server" + msg_to_send 
		s14.connect((Server_TCP_IP, 5004))
		s14.send(msg_to_send)
		s14.recv(1024)
		s14.close()
	except socket.error,msg:
		pass
	ack += 1

def q_thread():
	while True:
		temp_len_q = len(q)
		if(temp_len_q > 0):
			print "length of dict", temp_len_q
			global ack
			ack = 0
			thread.start_new_thread(q1_thread, ())
			thread.start_new_thread(q2_thread, ())
			thread.start_new_thread(q3_thread, ())
			thread.start_new_thread(q4_thread, ())
			time.sleep(0.3)
			while (ack != 4):
#				print ack
				pass
			print q
			q.pop()	
			print "after pop", q
			
thread.start_new_thread(q_thread, ())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, int(TCP_PORT)))
s.listen(1)

#this will do the listening part and print incoming messagaes
while 1:
	conn, addr = s.accept()
	data = conn.recv(int(BUFFER_SIZE))
	if data:
		data = data.rstrip('\n')
		temp_recv_data = data.split(' ')
		command = temp_recv_data[0]
		if(len(temp_recv_data) >= 2):
			Key = int(temp_recv_data[1])
		if(len(temp_recv_data) >= 3):	
			Value = int(temp_recv_data[2])
		if(len(temp_recv_data) >= 4):
			sender_server = int(temp_recv_data[3]) 	

		if (command == "delete"):					#Delete info with key from all replicas
			msg_to_send = "delete"
			msg_to_send = msg_to_send + ' '
			msg_to_send = msg_to_send + str(Key)
			q.append([msg_to_send, sender_server])
			
		elif (command == "get"):
			msg_to_send = "get"
			msg_to_send = msg_to_send + ' '
			msg_to_send = msg_to_send + str(Key)
			q.append([msg_to_send, sender_server])
					
		elif (command == "insert"):
			msg_to_send = "insert"
			msg_to_send = msg_to_send + ' '
			msg_to_send = msg_to_send + str(Key)
			msg_to_send = msg_to_send + ' '
			msg_to_send = msg_to_send + str(Value)
			print "msg_to_semd", msg_to_send
			q.append([msg_to_send, sender_server])
									
		elif (command == "update"):
			msg_to_send = "update"
			msg_to_send = msg_to_send + ' '
			msg_to_send = msg_to_send + str(Key)
			msg_to_send = msg_to_send + ' '
			msg_to_send = msg_to_send + str(Value)
			q.append([msg_to_send, sender_server])

		else:
			print "wrong command sent to central server"		
conn.close()
