from datetime import datetime, timedelta
import re
from string import Template
import subprocess
import sys

from pytimeparse.timeparse import timeparse

sys.path.append('/home/ziegs/.i3/py3status')
from py3base import py3base, py3main

# http://stackoverflow.com/a/8907269/228534.
class DeltaTemplate(Template):
  """Template to help format timedelta in the same manner as datetime."""
  delimiter = '%'
  idpattern = '[DMHS]'

def strfdelta(tdelta, fmt):
  """Formats a timedelta using the same tokens as strftime."""
  d = {'D': tdelta.days}
  d['H'], rem = divmod(tdelta.seconds, 3600)
  d['M'], d['S'] = divmod(rem, 60)
  t = DeltaTemplate(fmt)
  return t.substitute(**d)


class Py3status(py3base):
  """A py3status module to show the state of prodaccess."""

  format = '{expires} ({remaining})'
  # How to format the time remaining, e.g. 12h 20m
  format_remaining = '%Hh %Mm'
  # How to format the time at which prodaccess expires
  format_expires = '%H:%M'
  # How to format no prodaccess
  format_error = 'prodaccess'
  # Warn when approaching only so long left before expiry
  warning_time = '1h'
  cache_timeout = '1m'

  def _output(self):
    proc = subprocess.Popen(['/usr/bin/prodcertstatus'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out, err = proc.communicate()
    try:
      remaining_str = re.search('LOAS2 cert expires in (.+)', out.strip()).group(1)
      remaining = timedelta(seconds=timeparse(remaining_str))
      exitcode = proc.returncode
    except AttributeError: # 'NoneType' object has no attribute 'group'
      return {
        'full_text': self.format_error,
        'color': 'bad'
      }

    if exitcode != 0 or err.strip():
      raise RuntimeError(err)

    warn = remaining.total_seconds() < timeparse(self.warning_time)
    return {
      'full_text': self.format.format(
        expires=(datetime.now() + remaining).strftime(self.format_expires),
        remaining=strfdelta(remaining, self.format_remaining)),
      'color': 'degraded' if warn else 'good',
    }

# For testing, run python prodaccess.py [format=value] ...
py3main(Py3status(), __name__)
