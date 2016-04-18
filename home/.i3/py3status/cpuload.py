import os
import sys

sys.path.append('/home/ziegs/.i3/py3status')
from py3base import py3base, py3main

class Py3status(py3base):
  """A py3status module to show the current CPU load."""
  format = '{min1} {min5} {min15}'
  threshold_warn = 5.0
  threshold_danger = 8.0
  cache_duration = '1m'

  def _wrap(self, load):
    loadstr = '%0.2f' % load
    if load > float(self.threshold_danger):
      return '<span color="%s">%s</span>' % (
        self.i3status_config['color_bad'],
        loadstr
      )
    if load > float(self.threshold_warn):
      return '<span color="%s">%s</span>' % (
        self.i3status_config['color_degraded'],
        loadstr
      )
    return loadstr

  def _output(self):
    loadavg = os.getloadavg()
    return self.format.format(
      min1=self._wrap(loadavg[0]),
      min5=self._wrap(loadavg[1]),
      min15=self._wrap(loadavg[2]))

# For testing, run python cpuload.py [format=value] [threshold_warn=value] ...
py3main(Py3status(), __name__)
