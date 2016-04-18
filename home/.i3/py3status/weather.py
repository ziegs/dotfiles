import json
import sys
import urllib2

sys.path.append('/home/ziegs/.i3/py3status')
from py3base import py3base, py3main

# Get your API key here: http://home.openweathermap.org/users/sign_up.
API_KEY = '44db6a862fba0b067b1930da0d769e98'
URL_TEMPLATE = 'http://api.openweathermap.org/data/2.5/weather?id=%s&units=%s&appid=%s'

class Py3status(py3base):
  """A py3status module to show the current weather."""
  cache_timeout = '10m'
  # How to format the weather. See final line in _output for available values.
  format = '{condition} {temperature}F'
  # Units: "imperial", "metric", or "standard".
  units = 'imperial'
  city_id = '5799841'

  # Icon indices. The condition at position i in this list will return the
  # character at position i in the "icon_str" string.
  condition_index = [
    '01', # Clear
    '02', # Partly Cloudy
    '03', # Mostly Cloudy
    '04', # Cloudy
    '09', # Light Rain
    '10', # Rain
    '11', # Thunderstorm
    '13', # Snow
    '50', # Mist
  ]

  # A list of comma separated format strings.
  # Each index corresponds to the condition in the list above, and a single
  # condition string may use ':' to separate day and night conditions.
  condition_str = 'Clear Day:Clear Night,Partly Cloudy,Mostly Cloudy,Cloudy,Light Rain,Rain,Thunderstorm,Snow,Mist'

  def _get(self):
    """Get the weather from the API."""
    url = URL_TEMPLATE % (self.city_id, self.units, API_KEY)
    return urllib2.urlopen(url).read()

  def _output(self):
    """Returns the output for this module."""
    wjson = json.loads(self._get())
    icon = wjson['weather'][0]['icon']
    # Icon is of the form ##d or ##n based on day/night.
    # Use the first two characters to determine the condition.
    condition_idx = self.condition_index.index(icon[0:2])
    current_condition_str = self.condition_str.split(',')[condition_idx]
    # And if there are separate strings for day and night, use the last
    # character to choose between then.
    if ':' in current_condition_str:
      day_or_night = icon[-1]
      day, night = current_condition_str.split(':')
      if day_or_night == 'd':
        current_condition_str = day
      else:
        current_condition_str = night

    return self.format.format(
      temperature=wjson['main']['temp'],
      pressure=wjson['main']['pressure'],
      humidity=wjson['main']['humidity'],
      windspeed=wjson['wind']['speed'],
      winddirection=wjson['wind']['deg'],
      location=wjson['name'],
      condition=current_condition_str)

# For testing, run python weather.py [city_id=value] [units=value] ...
py3main(Py3status(), __name__)
