#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import datetime

print "Content-Type: text/html"
print

body = """<html>
<head>
<title>Lab A - CGI experiments</title>
</head>
<body>

The server IP address is %s:%s.<br>
<br>
The server name is %s. (if an IP address, then a DNS problem) <br>
<br>
You are coming from  %s:%s.<br>
<br>
Your hostname is %s.  <br>
<br>
The currenly executing script is %s<br>
<br>
The request arrived at %s<br>


</body>
</html>""" % (os.environ['LOCAL_ADDR'], # server IP
        os.environ['SERVER_PORT'], # server port
        os.environ['SERVER_NAME'], # server hostname
        os.environ['REMOTE_ADDR'], # client IP
        ''                       , # client port
        os.environ['REMOTE_HOST'], # client hostname
        os.environ['SCRIPT_NAME'], # this script name
        datetime.datetime.now(), # time
        )

print body,
"""
for key in os.environ.keys():
    print 'Key=%s, Value=%s' % (key, os.environ[key])
"""

