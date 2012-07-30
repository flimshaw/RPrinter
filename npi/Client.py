import socket

HOST = 'localhost'
PORT = 12311

class Client:

	def __init__(self):
		print "NPI client started."

	def connect(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, PORT))
		s.send('Hello, world')
		data = s.recv(1024)
		s.close()
		print 'Received', repr(data)