#!C:\Python26\python.exe
import cgi
import json
import re
import time
import cgitb; cgitb.enable(display=0, logdir="logs"); #used for debugging

print "Content-Type: application/json\n"

form = cgi.FieldStorage()

#set 'result' to sum of numbers from request parameters
keys = form.keys()
if len(keys) >= 2:
   a = form.getvalue(keys[0])
   b = form.getvalue(keys[1])
   if (re.match('\d', a) and re.match('\d', b)):
      result = int(a) + int(b)
   else:
      raise TypeError('At least one parameter is not a number')
else:
   raise KeyError('At least two keys required in the request parameters')

#set 'time'
time = time.time()

#set 'uwnetid'
uwnetid = 'jakenewf'

#pretty print response in json encoding
print json.dumps({'result': result, 'uwnetid': uwnetid, 'time': time}, \
                 indent=4)

#optional: example code for handling code exceptions individually
#in place of 'cgitb.enable()'
try:
   #insert some code besides pass
   pass
except:
   cgitb.handler()
