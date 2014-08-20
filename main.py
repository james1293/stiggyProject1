main.py
import webapp2
from google.appengine.api import urlfetch


class MainHandler(webapp2.RequestHandler):

  def get(self):  # pylint:disable-msg=invalid-name
    """Handle GET requests."""
    # self.response.headers['Content-Type'] = 'text/plain'

    self.response.write("""Hello, world.""")
    url = "http://www.google.com/"
    result = urlfetch.fetch(url)
    #if result.status_code == 200:
      #self.response.write((result.content)



APP = webapp2.WSGIApplication([('/', MainHandler)])

