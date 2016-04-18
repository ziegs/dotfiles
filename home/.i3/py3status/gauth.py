import httplib2
import os

from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow

client_id = '1053644992053-cirpgk09op3uiunlau6s5k8eb03rjkck.apps.googleusercontent.com'
client_secret = 'ISnPggXeyMBRbW9Bdevl3HUn'

# The scopes to authorise so that all py3status modules work.
SCOPES = [
  'https://www.googleapis.com/auth/calendar',
  'https://mail.google.com/',
  'https://www.googleapis.com/auth/gmail.labels',
  'https://www.googleapis.com/auth/gmail.readonly',
]

def google(service, version, **kwargs):
  storage = Storage(os.path.expanduser('~/.googlekeys/oauth2.dat'))
  credentials = storage.get()
  if credentials is None or credentials.invalid:
    raise RuntimeError('Auth error!')
  http = httplib2.Http()
  http = credentials.authorize(http)
  service = build(service, version, http=http)
  return service

def main():
  storage = Storage(os.path.expanduser('~/.googlekeys/oauth2.dat'))
  flow = OAuth2WebServerFlow(client_id, client_secret, SCOPES)
  credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

if __name__ == '__main__':
  main()
