from scapy.all import *
import time 
import socket
import time
import concurrent.futures
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-p',"--ports", nargs='+', help="type the ports you want to scan. Example : -p 22 23 80 133",type=int,required=True)
parser.add_argument("-t","--target",help="type here the target. Example : -t domain.com or , -t 1.1.1.1",type=str,required=True)

args = vars(parser.parse_args())

ip = socket.gethostbyname(args["target"])

def tcp_scan(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.2)
	if not sock.connect_ex((ip, port)) :
		print(f"Port {port} is open")

def main() :
	with concurrent.futures.ThreadPoolExecutor() as executor: 
		for scan in args["ports"] :
			executor.submit(tcp_scan,scan)
	
if __name__ == "__main__" :
	main()

