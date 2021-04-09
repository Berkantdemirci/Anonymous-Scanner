import requests
import os
import concurrent.futures
import time 

top_100_ports = [7,9,13,21,22,23,25,26,37,53,79,80,81,88,106,110,111,113,119,135,139,143,144,179,199,389,427,443,444,445,465,513,514,515,543,544,548,554,587,631,646,873,990,993,995,1025,1026,1027,1028,1029,1110,1433,1720,1723,1755,1900,2000,2001,2049,2121,2717,3000,3128,3306,3389,3986,4899,5000,5009,5051,5060,5101,5190,5357,5432,5631,5666,5800,5900,6000,6001,6646,7070,8000,8008,8009,8080,8081,8443,8888,9100,9999,10000,32768,49152,49153,49154,49155,49156,49157]
target = input("ip or domain (example : domain.com): ")

def scan(ports) :
    port = list(map(str,ports))
    port = " ".join(port)
    os.system(f"proxychains python3 tcp_scan.py -t {target} -p " + port)

def main() :
    with concurrent.futures.ThreadPoolExecutor() as executor :
        p = executor.submit(scan,top_100_ports[:25])
        p2 = executor.submit(scan,top_100_ports[25:50])
        p3 = executor.submit(scan,top_100_ports[50:75])
        p4 = executor.submit(scan,top_100_ports[75:])


if __name__ == "__main__" :
    os.system("proxychains python3 toripchecker.py")
    main()