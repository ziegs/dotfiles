import sys
sys.path.append('/home/ziegs/.i3/py3status')
from py3base import py3base, py3main

class Py3status(py3base):
  """A py3status module to show the current CPU temperature."""
  # This file should return the cpu temperature in thousandths of degree C.
  device = '/sys/class/thermal/thermal_zone0/temp'
  format = '{celcius} C / {fahrenheit} F / {kelvin} K'
  format_error = 'Error'
  # Warns when temperature is over this value.
  threshold_warn = '60c'
  # Error when temperature is over this value.
  threshold_danger = '70c'
  # Urgent when temperature is over this value.
  threshold_critical = '90c'

  def _parse_temp(self, temp):
    """Parse a temperature string (e.g. '50c', '90f') as degrees centigrade."""
    unit = temp[-1:].lower()
    value = int(temp[:-1])
    if unit == 'c':
      return value
    elif unit == 'f':
      return (value - 32) * 5 / 9
    elif unit == 'k':
      return value - 273.15
    raise ValueError('Cannot parse %s as a temperature' % temp)

  def _output(self):
    temp = None
    with open(self.device, 'r') as tempf:
      temp = int(tempf.read()) / 1000
    if not temp:
      return {'full_text': self.format_error, 'color': 'bad'}

    color = None
    urgent = False
    if temp > self._parse_temp(self.threshold_warn):
      color = 'degraded'
    if temp > self._parse_temp(self.threshold_danger):
      color = 'bad'
    if temp > self._parse_temp(self.threshold_critical):
      urgent = True

    return {
        'full_text': self.format.format(
          celcius=temp,
          centigrade=temp,
          fahrenheit=temp * 9 / 5 + 32,
          kelvin=temp + 273.15,
        ),
        'color': color,
        'urgent': urgent,
    }

# For testing, run python cputemp.py [device=value] [threshold_warn=value] ...
py3main(Py3status(), __name__)
