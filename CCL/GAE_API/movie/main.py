import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = []
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        filmname = self.request.get('filmName')
        url = "https://ghibliapi.herokuapp.com/films?title=" + filmname
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        title = data[0]['title']
        director = data[0]['director']
        producer = data[0]['producer']
        releaseDate = data[0]['release_date']

        template_values = {
            "title": title,
            "director": director,
            "producer": producer,
            "releaseDate": releaseDate  
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)