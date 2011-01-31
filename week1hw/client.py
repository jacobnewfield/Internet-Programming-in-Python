import socket 

host = 'localhost' 
#host = 'jakenewf@block115394-lrq.blueboxgrid.com'
port = 50011 
size = 1024
sdata = 0
s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port))  
while True:
	sdata = raw_input('\nEnter two integers, space dilimited: ')
	if len(sdata.split()) == 2 and sdata.split()[0].isdigit() and sdata.split()[1].isdigit():
		s.send(sdata)
		break
	else:
		print 'Exactly two integers required...'
data = s.recv(size)
s.close() 
if data:
	print 'Sum =', repr(data)
