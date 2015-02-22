#!/usr/bin/env python

import socket
import sys
import thread
import threading
import time
import readline
import io
import random
#from thread import *
#from threading import Thread
#from time import sleep

f=open('config4.txt')
lines=f.readlines()

TCP_IP = lines[1].rstrip('\n')
TCP_PORT = lines[2]
BUFFER_SIZE = lines[5]
aString = 'i am server1'

Server_TCP_IP = '127.0.0.1'

#Max delay time in seconds
MAX = lines[20]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, int(TCP_PORT)))
s.listen(1)

#defination of a thread to read a message
def get_msg():
	while True:
		aString = raw_input('')
		word = aString.split()
		firstWord = word[0]
		if firstWord=="Send":
			secondWord = word[1]
			thirdWord = word[2]
			wait_time = random.randint(0, int(MAX))						#pick a random number between 0 and MAX
			time.sleep(wait_time)									#delay for MAX seconds
			s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s1.connect((Server_TCP_IP, int(thirdWord)))
			s1.send(secondWord)
			s1.close()
			print "Sent %s to %s, system time is" %(secondWord, thirdWord)
#defination of thread to send a message to a specified address and port
def print_msg():
	while True:
		aString == raw_input('')
		#print aString
		s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s1.connect((Server2_TCP_IP, Server2_TCP_PORT))
		s1.send(aString)
		s1.close()

				
#creating a thread
thread.start_new_thread(get_msg, ())
#thread1.start_new_thread(print_msg, ())

#threads = []
#t = threading.Thread(target=print_msg)
#t.start()

#thread.start_new_thread(print_msg, ())
#t1 = threading.Thread(target=get_msg)
#threads.append(t1)
#t1.start()



#this will do the listening part and print incoming messagaes
while 1:
	conn, addr = s.accept()
	data = conn.recv(int(BUFFER_SIZE))
	if data:
		print "Received %s from %s, Max delay is , system time is" % (data, addr)
conn.close()
