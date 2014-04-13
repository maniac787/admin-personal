import os

from google.appengine.ext.webapp import template
import webapp2

class LoginBean (webapp2.RequestHandler):
    def get(self):
        print('sd')
        temp = os.path.join(os.path.dirname(__file__), 'templates/login.html')
        outstr = template.render(temp, {'resp': 'Buena Suerte', 'prueba':'Hola mundo'})
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(outstr)
    def post(self):


        temp = os.path.join(os.path.dirname(__file__), 'templates/estimacion.html')
        outstr = template.render( temp, {'real': 'msg', 'estimacion': 'estimacion'})
        self.response.out.write(outstr)

app = webapp2.WSGIApplication([('/login.html', LoginBean)], debug=True)