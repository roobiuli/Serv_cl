#!/usr/bin/python
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_port = int
login = False
if len(sys.argv) == 2:
    server_port = int(sys.argv[1])
elif len(sys.argv) == 4:
    print '4'
    if sys.argv[2] == '-l':
        server_port = int(sys.argv[1])
        logFile = sys.argv[3]
        logs = ""
        loging = True
    else:
        print 'Please provide the correct arguments'
else:
    print 'Please provide the correct arguments' 

server_address = ('localhost', server_port)
print >>sys.stderr, 'Connecting to %s port %s' % server_address
sock.connect(server_address)

while True:

    try:
        data = raw_input("Please enter a command: ")
        sock.sendall(data)
        if loging:
            log = logs += data
            open(logFile, "w")
            write(log)



        #data = sock.recv(1024)
        #if logging:
         #   logs += data
            
        if data == 'exit':
            print 'Client closing'
            break
        elif data == '404':
            print 'Command not found'
        elif data == 'File not found':
            print 'File not found'
            continue
        else:
            data = sock.recv(1024)
            print data
            continue
            sys.stout.close()
            continue
    finally:
        'Something went wrong'

    