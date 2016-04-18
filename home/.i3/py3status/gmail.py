import re
import sys
from xml.sax.saxutils import escape

sys.path.append('/home/ziegs/.i3/py3status')
# on 'Auth error!', run `python gauth.py` to set up credentials.
from gauth import google
from py3base import py3base, py3main


class Py3status(py3base):
  """A py3status module to show the unread count of gmail."""
  cache_duration = '6m'
  # How to format the unread count.
  format = '{INBOX} unread'
  # Warning when more than this many emails unread.
  warning_count = 5
  # Whether to hide unread when zero.
  hide_if_zero = True

  def _output(self):
    labels = google('gmail', 'v1').users().labels()
    total_unread = 0
    unread_counts = {}
    for label in re.findall(r'\{(\w+)\}', self.format):
      unread_count = labels.get(userId='me', id=label, fields='threadsUnread').execute().get('threadsUnread', 0)
      total_unread += unread_count
      if unread_count >= self.warning_count:
        unread_counts[label] = '<span color="%s">%d</span>' % (
            self.i3status_config['color_degraded'],
            unread_count
          )
      else:
        unread_counts[label] = '%d' % unread_count

    if total_unread or not self.hide_if_zero:
      return self.format.format(**unread_counts)
    return ''

# For testing, run python gmail.py [format=value] ...
py3main(Py3status(), __name__)
