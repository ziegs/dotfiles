from datetime import datetime, timedelta
from dateutil.parser import parse
from dateutil.tz import tzlocal
import os
import sys
from xml.sax.saxutils import escape

from pytimeparse.timeparse import timeparse

sys.path.append('/home/ziegs/.i3/py3status')
# on 'Auth error!', run `python gauth.py` to set up credentials.
from gauth import google
from py3base import py3base, py3main


class Py3status(py3base):
  """A py3status module to show upcoming events from Google Calendar."""
  cache_timeout = '3m'
  # How long to show current events for before switching to the next event
  elapsed_margin = '5m'
  # Max time to look ahead for
  search_time = '18h'
  # How to format the event for i3
  format = '{start}-{end}: {summary}@{location}'
  format_urgent = '{start}-{end}: {summary}@{location}'
  time_format = '%H:%M'
  # Calendar to use
  calendar_id = 'primary'
  # Relative times
  relative_ago = '%s ago'
  relative_in = 'in %s'
  relative_now = 'now'
  # Default warning time
  warning_time = '7m'
  # Only colour events if they start in less than this time
  highlight_time = '2h'
  # Command to execute when clicked
  notify_command = 'notify-send "{start}-{end}: {summary}" "{location}"'

  _next_event = None

  def _print_relative(self, seconds):
    """Prints a relative time string for the given number of seconds.
    e.g. '1d 1h', or '2h 5m'"""
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
      return '%dd %dh' % (days, hours)
    elif hours > 0:
      return '%dh %dm' % (hours, minutes)
    elif minutes > 0:
      return '%dm' % minutes
    else:
      return '%ds' % seconds

  def _relative(self, date):
    """Gets the relative time of `date` from now, as a formatted string.
    e.g. 'in 2h 5m', or '7h ago'."""
    now = datetime.now(tz=tzlocal())
    delta = (date - now).total_seconds()
    if abs(delta) < 60:
      return self.relative_now
    elif delta < 0:
      return self.relative_ago % (self._print_relative(-delta))
    else:
      return self.relative_in % (self._print_relative(delta))

  def _format_event(self, format_str, event=None):
    """Formats a string with the event's parameters."""
    event = event or self._next_event
    return format_str.format(
      start=event['start'].strftime(self.time_format),
      end=event['end'].strftime(self.time_format),
      summary=event['summary'],
      location=event['location'],
      status=event['status'],
      relative=self._relative(event['start']),
    )

  def on_click(self, unused_json, unused_config, evt):
    """When left-clicked, sends a system notification for the next event."""
    if not self._next_event:
      return
    if evt.get('button', 0) != 1:
      return
    notify_command = self._format_event(self.notify_command)
    os.system(notify_command)

  def _output(self):
    now = datetime.now(tz=tzlocal())
    timeMin = now - timedelta(seconds=timeparse(self.elapsed_margin))
    timeMax = now + timedelta(seconds=timeparse(self.search_time))
    request = google('calendar', 'v3').events().list(
      calendarId=self.calendar_id,
      timeMin=timeMin.strftime("%Y-%m-%dT%H:%M:%S%z"),
      timeMax=timeMax.strftime("%Y-%m-%dT%H:%M:%S%z"),
      maxAttendees=1,
      maxResults=10,
      orderBy='startTime',
      showDeleted=False,
      showHiddenInvitations=False,
      singleEvents=True,
      fields='items(end,location,start,status,summary,attendees,reminders)'
    )
    response = request.execute()
    event = None
    for e in response.get('items', []):
      e['start'] = parse(e['start']['dateTime'])
      e['end'] = parse(e['end']['dateTime'])
      if e['start'] < timeMin:
        continue
      e['responseStatus'] = e.get('attendees', [{}])[0].get('responseStatus', 'unknown') if e['responseStatus'] == 'cancelled' or e['responseStatus'] == 'declined':
        continue
      event = e
      break
    # For notifications
    self._next_event = event

    full_text = ''
    color = None
    urgent = False

    if event:
      if event['start'] < now and event['end'] > now:
        color = 'degraded'
      elif event['start'] > now:
        if (now - event['start']).total_seconds() < timeparse(self.highlight_time):
          color = 'good'

      if e['responseStatus'] == 'accepted' or e['responseStatus'] == 'tentative':
        warning_time = timedelta(seconds=timeparse(self.warning_time))
        for reminder in event['reminders'].get('overrides', []):
          if warning_time.total_seconds() < reminder['minutes'] * 60:
            warning_time = timedelta(minutes=reminder['minutes'])
        if event['start'] - now < warning_time:
          urgent = True

      format_str = self.format
      if urgent:
        format_str = self.format_urgent

      for key in ['summary', 'location', 'status']:
        event[key] = escape(event.get(key, ''))

      full_text = self._format_event(format_str)

    return {
        'full_text': full_text,
        'color': color,
        'urgent': urgent,
     }

# For testing, run python gcalendar.py [calendar_id=value] [format=value] ...
py3main(Py3status(), __name__)
