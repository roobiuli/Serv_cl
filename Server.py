#!/usr/bin/python
import socket
import sys
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_port = int(sys.argv[1])
server_address = ('localhost', server_port)
print >>sys.stderr, 'starting up on %s port %s' % server_address

sock.bind(server_address)
sock.listen(1)

def listCurrentDir():
    data = os.listdir('.')
    stringData = ', '.join(data)
    connection.sendall(stringData)

def catFile(data):
	filePath = data.split()
	print os.path.isfile(filePath[1])
	if os.path.isfile(filePath[1]):
		print 'Sending', filePath[1]
		fileContent = open(filePath[1], 'rb')
		l = fileContent.read(1024)
		while (l):
			connection.send(l)
			l = fileContent.read(1024)

		fileContent.close()
		print "Done Sending"
	else:
		connection.sendall('File not found')
##
while True:
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'A new connection established:', client_address
        while True:
            data = connection.recv(1024)

            if data == 'exit':
            	connection.sendall('exit')
                connection.close()
                break
            #elif data == 'ls':
            elif data == 'ls':
            	listCurrentDir()
            	continue
            elif 'cat ' in data:
            	catFile(data)
                continue
            else:
            	connection.sendall('404')
            	continue
    finally:
    	print 'Server closing'
    	break