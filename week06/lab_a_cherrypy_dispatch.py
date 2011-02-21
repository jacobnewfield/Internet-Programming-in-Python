import cherrypy

class HelloWorld:
    @cherrypy.expose
    def index(self):
        yield 'Hello CherryPy world!'
        yield '<br/>'
        yield '<br/><a href="/link_a/">link a</a>'
        yield '<br/><a href="/link_b/">link b</a> - should work like link a'
        yield '<br/>'
        yield '<br/><a href="/positional/first/">/positional/first/</a>'
        yield '<br/><a href="/positional/first/second/">/positional/first/second/</a>'
        yield '<br/><a href="/positional/first/second/third/">/positional/first/second/third/</a>'
        yield '<br/><a href="/positional/first/second/third/fourth/">/positional/first/second/third/fourth/</a>'
        yield '<br/>'
        yield '<br/><a href="/named?a=spam">/named?a=spam</a>'
        yield '<br/><a href="/named?a=spam&b=eggs">/named?a=spam&b=eggs</a>'
        yield '<br/><a href="/named?a=spam&b=eggs&c=ham">/named?a=spam&b=eggs&c=ham</a>'
    @cherrypy.expose
    def link_a(self):
        yield 'hello from link a'

    @cherrypy.expose
    def link_b(self):
        yield 'hello from link b'

    @cherrypy.expose
    def positional(self, *args):
        yield 'look, arguments!<br/>'
        for arg in args:
            yield arg + '<br>'
        yield '<br/>'


    @cherrypy.expose
    def named(self, **kwargs):
        yield 'look, keyword arguments!<br/>'
        yield '<table border="1">'
        for key in kwargs:
            yield '<tr><td>%s</td><td>%s</td></tr>' % (key, kwargs[key])
        yield '</table>'
cherrypy.quickstart(HelloWorld())

