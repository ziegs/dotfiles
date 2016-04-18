from datetime import datetime
import dateutil.parser
import sys

from pytz import timezone

# Needed to avoid install py3base in site-packages.
sys.path.append('/home/ziegs/.i3/py3status')
from py3base import py3base, py3main

class Py3status(py3base):
  """A py3status module to show working hours in a given timezone."""

  # How to format the time.
  format = '%H:%M'
  format_warn = '! %H:%M'
  format_not_working = 'X %H:%M'
  # The timezone to use.
  timezone = "Europe/London"
  # Whether to hide the time when outside working hours.
  hide_if_not_working = False

  # Control the colour of the output:
  start_warn = "9:00"
  # Warn between start_warn and start,
  start = "10:00"
  # Good between start and end,
  end = "18:00"
  # Warn again between end and end_warn,
  end_warn = "20:00"
  # And Bad all other times.

  def _tbetw(self, now, start, end):
    """Returns true if `now` is between `start` and `end`.
    Accounts for start being after end, i.e., midnight issues and day wraps."""
    if start <= end:
      return start < now < end
    else:
      return now < end or now > start

  def _parse_in_tz(self, time_str):
    """Parses `time_str` as a datetime in the module's timezone."""
    now_in_tz = datetime.now(tz=timezone(self.timezone))
    time_str += now_in_tz.strftime('%z')
    return dateutil.parser.parse(time_str)

  def _output(self):
    """Returns the output for this module."""
    now = datetime.now(tz=timezone(self.timezone))
    start_warn = self._parse_in_tz(self.start_warn)
    start = self._parse_in_tz(self.start)
    end = self._parse_in_tz(self.end)
    end_warn = self._parse_in_tz(self.end_warn)

    format = self.format
    color = 'good'
    if self._tbetw(now, start_warn, start) or self._tbetw(now, end, end_warn):
      color = 'degraded'
      if self.format_warn:
        format = self.format_warn
    elif not self._tbetw(now, start, end):
      color = 'bad'
      if self.hide_if_not_working:
        format = ''
      elif self.format_not_working:
        format = self.format_not_working

    return {
      'full_text': now.strftime(format),
      'color': color,
    }

# For testing, run python working_hours.py [timezone=value] [start=value] ...
py3main(Py3status(), __name__)
