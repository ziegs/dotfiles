from datetime import datetime
import sys

sys.path.append('/home/ziegs/.i3/py3status')
from py3base import py3base, py3main

class Py3status(py3base):
  """A py3status module to show the current time."""
  format = '%H:%M'
  cache_timeout = '1s'

  def _output(self):
    return datetime.now().strftime(self.format)

# For testing, run python localtime.py [format=value] ...
py3main(Py3status(), __name__)
