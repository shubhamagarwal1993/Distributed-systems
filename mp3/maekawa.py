#@created 24th April, 2015 SA
#
#!/usr/bin/env python
import socket, sys, thread, threading, time, readline, io, random, re, os, subprocess
#from nodes import process_1, process_2, process_3, process_4, process_5, process_6, process_7, process_8, process_9 
from threading import Thread
cs_int = 5
next_req = 5
tot_exec_time = 13
process_1_state = 'RELEASED'
process_1_voted = 'FALSE'
process_2_state = 'RELEASED'
process_2_voted = 'FALSE'
process_3_state = 'RELEASED'
process_3_voted = 'FALSE'
process_4_state = 'RELEASED'
process_4_voted = 'FALSE'
process_5_state = 'RELEASED'
process_5_voted = 'FALSE'
process_6_state = 'RELEASED'
process_6_voted = 'FALSE'
process_7_state = 'RELEASED'
process_7_voted = 'FALSE'
process_8_state = 'RELEASED'
process_8_voted = 'FALSE'
process_9_state = 'RELEASED'
process_9_voted = 'FALSE'
process_1_queue = []
process_2_queue = []
process_3_queue = []
process_4_queue = []
process_5_queue = []
process_6_queue = []
process_7_queue = []
process_8_queue = []
process_9_queue = []

def code_exit():
	global tot_exec_time
	time.sleep(int(tot_exec_time))
	print "Bye..!"
	os._exit(0)
	print "hahahahaha"
#thread.start_new_thread(code_exit, ())

TCP_IP = '127.0.0.1'
TCP_PORT_MAIN = '8000'
TCP_PORT_PROCESS1 = '8001'
TCP_PORT_PROCESS2 = '8002'
TCP_PORT_PROCESS3 = '8003'
TCP_PORT_PROCESS4 = '8004'
TCP_PORT_PROCESS5 = '8005'
TCP_PORT_PROCESS6 = '8006'
TCP_PORT_PROCESS7 = '8007'
TCP_PORT_PROCESS8 = '8008'
TCP_PORT_PROCESS9 = '8009'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, int(TCP_PORT_MAIN)))
s.listen(1)
#----------------------------------------------------------------------------------------------------
def send_thread_at_will(msg, dest):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
	s.connect(('', int(dest)))
	s.send(msg)
	s.close()
	

class processes:
	def __init__(self):
		pass
	def process_init(self):
		self.state = 'RELEASED'
		self.voted = 'FALSE'
#	def listen(self):
#		while True:
#			conn, addr = s.accept()
#			data = conn.recv(1024)
#			if data:
#				data = data.rstrip('\n')
#				print "data recv is ", data
#				if (data == 'poked you'):
#					print "have to send back acknowledgement"
#		conn.close()						
	def request(self):
		state = 'WANTED'
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((TCP_IP, 8000))
			s.send('poked you')
			t = s.recv(1024)
			print t
			s.close
			if (thread1_request_ack == 8):
				state = 'HELD'
		except socket.error,msg:
			pass
	def exit(self):
		state = 'RELEASED'
		#HAVE TO SEND RELEASE MSG TO ALL THE PROCESSES
class Node:
	def __init__(self):
		pass
#-------------------------------------------------------------------------------------------------
def process_1_listen():
	global process_1_state, process_1_voted, process_1_queue
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, int(TCP_PORT_PROCESS1)))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		if data:
			data = data.rstrip('\n')	
			words = data.split(' ')
			if (int(words[2]) != 8001):
				if (words[0] == 'ping'):
					if ((process_1_state == 'HELD') or (process_1_voted == 'TRUE')):
						process_1_queue.append(int(words[2]))
					else:
						Thread(target = send_thread_at_will, args=('pong 1 8001', int(words[2]))).start()
						process_1_voted = 'TRUE'
				elif (words[0] == 'release'):
					if not process_1_queue:
						process_1_voted = 'FALSE'
					else:
						Thread(target = send_thread_at_will, args=('token 1 8001', int(words[2]))).start()
						process_1_votes = 'TRUE'
						process_1_queue.pop()	
				elif (words[0] == 'pong'):
					pass
				elif (words[0] == 'token'):
					pass		
				else:
					print "dont send me crap in 1"
					pass
			else:
				pass		
	conn.close()

def process_2_listen():
	global process_2_state, process_2_voted, process_2_queue
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, int(TCP_PORT_PROCESS2)))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)		
		if data:
			data = data.rstrip('\n')	
			words = data.split(' ')
			if (int(words[2]) != 8002):
				if (words[0] == 'ping'):
					if ((process_2_state == 'HELD') or (process_2_voted == 'TRUE')):
						process_2_queue.append(int(words[2]))
					else:
						Thread(target = send_thread_at_will, args=('pong 2 8002', int(words[2]))).start()
						process_2_voted = 'TRUE'
				elif (words[0] == 'release'):
					if not process_2_queue:
						process_2_voted = 'FALSE'
					else:
						Thread(target = send_thread_at_will, args=('token 2 8002', int(words[2]))).start()
						process_2_votes = 'TRUE'
						process_2_queue.pop()	
				elif (words[0] == 'pong'):
					pass
				elif (words[0] == 'token'):
					pass		
				else:
					print "dont send me crap"
					pass
			else:
				pass		
	conn.close()

def process_3_listen():
	global process_3_state, process_3_voted, process_3_queue
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, int(TCP_PORT_PROCESS3)))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		if data:
			data = data.rstrip('\n')	
			words = data.split(' ')
			if (int(words[2]) != 8003):
				if (words[0] == 'ping'):
					if ((process_3_state == 'HELD') or (process_3_voted == 'TRUE')):
						process_3_queue.append(int(words[2]))
					else:
						Thread(target = send_thread_at_will, args=('pong 3 8003', int(words[2]))).start()
						process_3_voted = 'TRUE'
				elif (words[0] == 'release'):
					if not process_3_queue:
						process_3_voted = 'FALSE'
					else:
						Thread(target = send_thread_at_will, args=('token 3 8003', int(words[2]))).start()
						process_3_votes = 'TRUE'
						process_3_queue.pop()
				elif (words[0] == 'pong'):
					pass
				elif (words[0] == 'token'):
					pass	
				else:
					print "dont send me crap"
					pass
			else:
				pass		
	conn.close()

def process_4_listen():
	global process_4_state, process_4_voted, process_4_queue
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, int(TCP_PORT_PROCESS4)))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		if data:
			data = data.rstrip('\n')	
			words = data.split(' ')
			if (int(words[2]) != 8004):
				if (words[0] == 'ping'):
					if ((process_4_state == 'HELD') or (process_4_voted == 'TRUE')):
						process_4_queue.append(int(words[2]))
					else:
						Thread(target = send_thread_at_will, args=('pong 4 8004', int(words[2]))).start()
						process_4_voted = 'TRUE'
				elif (words[0] == 'release'):
					if not process_4_queue:
						process_4_voted = 'FALSE'
					else:
						Thread(target = send_thread_at_will, args=('token 4 8004', int(words[2]))).start()
						process_4_votes = 'TRUE'
						process_4_queue.pop()	
				elif (words[0] == 'pong'):
					pass
				elif (words[0] == 'token'):
					pass
				else:
					print "dont send me crap"
					pass	
			else:
				pass		
	conn.close()
	
def process_5_listen():
	global process_5_state, process_5_voted, process_5_queue
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, int(TCP_PORT_PROCESS5)))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		if data:
			data = data.rstrip('\n')	
			words = data.split(' ')
			if (int(words[2]) != 8005):
				if (words[0] == 'ping'):
					if ((process_5_state == 'HELD') or (process_5_voted == 'TRUE')):
						process_5_queue.append(int(words[2]))
					else:
						Thread(target = send_thread_at_will, args=('pong 5 8005', int(words[2]))).start()
						process_5_voted = 'TRUE'
				elif (words[0] == 'release'):
					if not process_5_queue:
						process_5_voted = 'FALSE'
					else:
						Thread(target = send_thread_at_will, args=('token 5 8005', int(words[2]))).start()
						process_5_votes = 'TRUE'
						process_5_queue.pop()	
				elif (words[0] == 'pong'):
					pass
				elif (words[0] == 'token'):
					pass
				else:
					print "dont send me crap"
					pass
			else:
				pass		
	conn.close()
	
def process_6_listen():
	global process_6_state, process_6_voted, process_6_queue
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, int(TCP_PORT_PROCESS6)))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		if data:
			data = data.rstrip('\n')	
			words = data.split(' ')
			if (int(words[2]) != 8006):
				if (words[0] == 'ping'):
					if ((process_6_state == 'HELD') or (process_6_voted == 'TRUE')):
						process_6_queue.append(int(words[2]))
					else:
						Thread(target = send_thread_at_will, args=('pong 6 8006', int(words[2]))).start()
						process_6_voted = 'TRUE'
				elif (words[0] == 'release'):
					if not process_6_queue:
						process_6_voted = 'FALSE'
					else:
						Thread(target = send_thread_at_will, args=('token 6 8006', int(words[2]))).start()
						process_6_votes = 'TRUE'
						process_6_queue.pop()	
				elif (words[0] == 'pong'):
					pass
				elif (words[0] == 'token'):
					pass
				else:
					print "dont send me crap"
					pass
			else:
				pass		
	conn.close()

def process_7_listen():
	global process_7_state, process_7_voted, process_7_queue
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, int(TCP_PORT_PROCESS7)))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		if data:
			data = data.rstrip('\n')	
			words = data.split(' ')
			if (int(words[2]) != 8007):
				if (words[0] == 'ping'):
					if ((process_7_state == 'HELD') or (process_7_voted == 'TRUE')):
						process_7_queue.append(int(words[2]))
					else:
						Thread(target = send_thread_at_will, args=('pong 7 8007', int(words[2]))).start()
						process_7_voted = 'TRUE'
				elif (words[0] == 'release'):
					if not process_7_queue:
						process_7_voted = 'FALSE'
					else:
						Thread(target = send_thread_at_will, args=('token 7 8007', int(words[2]))).start()
						process_7_votes = 'TRUE'
						process_7_queue.pop()	
				elif (words[0] == 'pong'):
					pass
				elif (words[0] == 'token'):
					pass
				else:
					print "dont send me crap"
					pass
			else:
				pass		
	conn.close()

def process_8_listen():
	global process_8_state, process_8_voted, process_8_queue
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, int(TCP_PORT_PROCESS8)))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		if data:
			data = data.rstrip('\n')	
			words = data.split(' ')
			if (int(words[2]) != 8008):
				if (words[0] == 'ping'):
					if ((process_8_state == 'HELD') or (process_8_voted == 'TRUE')):
						process_8_queue.append(int(words[2]))
					else:
						Thread(target = send_thread_at_will, args=('pong 8 8008', int(words[2]))).start()
						process_8_voted = 'TRUE'
				elif (words[0] == 'release'):
					if not process_8_queue:
						process_8_voted = 'FALSE'
					else:
						Thread(target = send_thread_at_will, args=('token 8 8008', int(words[2]))).start()
						process_8_votes = 'TRUE'
						process_8_queue.pop()	
				elif (words[0] == 'pong'):
					pass
				elif (words[0] == 'token'):
					pass
				else:
					print "dont send me crap"
					pass
			else:
				pass		
	conn.close()

def process_9_listen():
	global process_9_state, process_9_voted, process_9_queue
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, int(TCP_PORT_PROCESS9)))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		if data:
			data = data.rstrip('\n')	
			words = data.split(' ')
			if (int(words[2]) != 8009):
				if (words[0] == 'ping'):
					if ((process_9_state == 'HELD') or (process_9_voted == 'TRUE')):
						process_9_queue.append(int(words[2]))
					else:
						Thread(target = send_thread_at_will, args=('pong 9 8009', int(words[2]))).start()
						process_9_voted = 'TRUE'
				elif (words[0] == 'release'):
					if not process_9_queue:
						process_9_voted = 'FALSE'
					else:
						Thread(target = send_thread_at_will, args=('token 1 8001', int(words[2]))).start()
						process_9_votes = 'TRUE'
						process_9_queue.pop()	
				elif (words[0] == 'pong'):
					pass
				elif (words[0] == 'token'):
					pass
				else:
					print "dont send me crap"
					pass
			else:
				pass		
	conn.close()
#--------------------------------------------------------------
def process_1():
	global cs_int, next_req, tot_exec_time, process_1_state, process_1_voted
	while True:
		#init
		process_1_state = 'RELEASED'
		process_1_voted = 'FALSE'
		#request
		time.sleep(int(next_req))
		process_1_state = 'WANTED'
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('', 8001))
		s.send('ping 1 8001')
		s.close()
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('', 8002))
		s.send('ping 1 8001')
		s.close()

		time.sleep(20)

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('', 8003))
		s.send('ping 1 8001')
		s.close()
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('', 8004))
		s.send('ping 1 8001')
		s.close()
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('', 8007))
		s.send('ping 1 8001')
		s.close()
		#held
		process_1_state = 'HELD'		
		time.sleep(int(cs_int))
		#exit
		process_1_state = 'RELEASED'
		#multicast release to all processes in condition		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		s.connect(('', 8001))
		s.send('release 1 8001')
		s.close()
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		s.connect(('', 8002))
		s.send('release 1 8001')
		s.close()
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		s.connect(('', 8003))
		s.send('release 1 8001')
		s.close()
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		s.connect(('', 8004))
		s.send('release 1 8001')
		s.close()
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		s.connect(('', 8005))
		s.send('release 1 8001')
		s.close()

#--------------------------------------------------------------------------------------------------
#this will do the listening part and print incoming messagaes
#a = processes()
#thread.start_new_thread(a.test, ())
thread.start_new_thread(process_1, ())
#thread.start_new_thread(process_2, ())
thread.start_new_thread(process_1_listen, ())
thread.start_new_thread(process_2_listen, ())
thread.start_new_thread(process_3_listen, ())
thread.start_new_thread(process_4_listen, ())
thread.start_new_thread(process_5_listen, ())
thread.start_new_thread(process_6_listen, ())
thread.start_new_thread(process_7_listen, ())
thread.start_new_thread(process_8_listen, ())
thread.start_new_thread(process_9_listen, ())
while 1:
	time.sleep(200)
	try:
		instruction = raw_input("")
		words = instruction.split()
		if (words == 'gogo'):
			print "gogo"		
		elif (words == 'nono'):
			print "nono"		
		else:
			print "dead end - something is wrong"
	except KeyboardInterrupt:	#ValueError:						#KeyboardInterrupt:
		break
		print "Bye"
