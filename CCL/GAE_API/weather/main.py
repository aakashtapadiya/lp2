import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        city = self.request.get('city')
        url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=26e1730ec6d79478f1ec39da4796ea0d&units=metric" % city
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        print(data)
        if(data['cod']=='404'):
            return self.response.out.write("Invalid City")
        weather = data['weather'][0]['description']
        weather = weather.capitalize()
        temp = data['main']['temp']
        pressure = data['main']['pressure']
        icon_id = data['weather'][0]['icon']
        speed = data['wind']['speed']
        print(weather)
        template_values = {
            "weather": weather,
            "temp": temp,
            "pressure": pressure,
            "speed": speed
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))
        
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
