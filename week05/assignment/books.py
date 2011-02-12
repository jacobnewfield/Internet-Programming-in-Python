#!/usr/bin/python2.6
import cherrypy
import os
import sys
#include current directory to module search path
sys.path.append(os.path.dirname(__file__))
from bookdb import BookDB
import cgitb; cgitb.enable(); #used for debugging

cherrypy.config.update({'environment': 'embedded'})

titles = sorted(BookDB().titles())

html_head = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<HTML>
<HEAD>
<TITLE>%s</TITLE>
<META NAME="Generator" CONTENT="TextPad 4.6">
<META NAME="Author" CONTENT="Jacob Newfield">
<META NAME="Keywords" CONTENT="books, bookdb, internet programming in python, assignment 05">
<META NAME="Description" CONTENT="Assignment 05 for UW class Internet Prorgramming in Python">
</HEAD>

<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#FF0000" VLINK="#800000" ALINK="#FF00FF" BACKGROUND=>
"""

html_tail = """\
</BODY>
</HTML>
"""
class Books(object):
    def index(self):
        t = 'Books Main Page'
        n = 0
        rstring = ''
        for title in titles:
            n += 1
            s = '<a href="details?id=id%s">%s</a><br>\n' % (n, title['title'])
            rstring += s
        return html_head % t + rstring + html_tail
    index.exposed = True

    def details(self, id):
        info = BookDB().title_info(id)
        t = "Details for Book '%s'" % info['title']
        home = '<a href="/">Home</a>'
        rstring = '<br>\n'.join(['%s: %s' % (key, info[key]) for key in info])
        return html_head % t + rstring + '<br>\n' + home + html_tail
    details.exposed = True
    
cherrypy.quickstart(Books())
#application = cherrypy.Application(Books(), script_name=None, config=None) 
