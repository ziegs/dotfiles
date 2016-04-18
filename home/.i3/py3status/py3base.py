import inspect
import os
import sys
from time import time

from pytimeparse.timeparse import timeparse

class py3base(object):
  """A base class for writing py3status modules.

  This base class abstracts away the i3status config, cache timeout, naming the
  output, and enables pango markup for all output.

  It also provides a `main()` method that allows testing from the command line
  with full support for configuration parameters.
  """
  cache_timeout = None

  def _output(self):
    raise NotImplementedError('Override `_output()` to return a dict!')

  def __init__(self):
    # Get the name of the file importing this class. That name is used as the
    # method name for the output function, per the py3status convention.
    calling_file_name = inspect.stack()[-1][1]
    self.name = os.path.splitext(calling_file_name)[0]
    self.__dict__[self.name] = self._output_function

  def _output_function(self, unused_json, i3status_config):
    """Takes the output from the subclass and formats it for py3status."""
    self.i3status_config = i3status_config
    try:
      output = self._output()
    except Exception as e:
      output = {
        'full_text': str(e),
        'color': 'bad',
      }
    # Subclasses may choose to simply return a string, so wrap it here.
    if isinstance(output, basestring):
      output = {'full_text': output}
    # Subclasses return 'color': 'bad', and we parse that here.
    if output.get('color', None):
      output['color'] = i3status_config['color_%s' % output['color']]
    # If a cache_timeout is defined, use that to set the 'cached_until'
    if self.cache_timeout:
      output['cached_until'] = time() + timeparse(self.cache_timeout)
    # All modules must output pango, unless they already define a markup.
    output['markup'] = output.get('markup', 'pango')
    output['name'] = self.name
    return output


class IdentityDict(dict):
  """A dict that returns the key for any getitem call.

  When passed as the i3config, this can help trace the use of various i3config
  parameters in the module output.
  """
  def __missing__(self, key):
    return key


def py3main(module, caller_name):
  """A method to run a py3module on the command-line.

  It supports 'parsing' the command line arguments in the form of name=value
  and using them to set configuration values for the module.
  """
  if caller_name != '__main__':
    return
  for argv in sys.argv[1:]:
    var, value = argv.split('=', 1)
    module.__dict__[var] = value
  print module._output_function(None, IdentityDict())
