import socket

host = ''		#Symbolic name meaning all available interfaces 
port = 50011
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
print '\nServer started\nWaiting for connection...\n'
while True: 
    conn, address = s.accept()
    print 'Connection established by client', address
    rdata = conn.recv(size)
    if rdata: 
    	nums = rdata.split()
	sum = int(nums[0]) + int(nums[1])
    	conn.send(repr(sum))
	print 'Sum sent to', address
    else:
    	print 'No data found'
    conn.close()
    print 'Connection closed\nWaiting for new connection...\n'
