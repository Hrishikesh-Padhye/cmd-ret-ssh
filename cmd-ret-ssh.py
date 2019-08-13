#!/usr/bin/python

import sys
from pexpect import pxssh

commands = len(sys.argv)

class Client:
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.session = self.connect()
	def connect(self):
		#This function is used to connect to the address using the given credentials.
		try:
			s = pxssh.pxssh()
			s.login(self.host, self.user, self.password)
			return s
		except Exception as e:
			print e
			print '[-] Error Connecting'
	def send_command(self, cmd):
		#This function sends the given command to the system for obtaining output.
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before

def botnetCommand(command):
		#This function executes the specified command and returns the console output.
		for client in botNet:
			output = client.send_command(command)
			print '[*] Output from ' + client.host
			print '[+] ' + output + '\n'

def addClient(host, user, password):
	#This function adds a client machine to our list of target machines.
	client = Client(host, user, password)
	botNet.append(client)
	
botNet = []
addClient('127.0.0.1', 'root', 'toor')	#Trying on localhost
#addClient('10.10.10.120', 'root', 'toor')
#addClient('10.10.10.130', 'root', 'toor')
for i in sys.argv[1:]:
	botnetCommand(str(i))	



	
	
