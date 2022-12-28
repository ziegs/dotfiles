#!/bin/bash

set -u

gcertstatus --ssh_cert_comment=corp/normal --check_remaining=1h > /dev/null 2>&1;
case $? in
  # gcert ok:
  0)
    echo '✓'
    echo '✓'
    echo '#00FF00'
    ;;
  # ssh cert will soon expire:
  8)
    echo '1H'
    echo '1H'
    echo '#FFFF00'
    ;;
  # No ssh cert:
  *)
    echo '✗'
    echo '✗'
    echo '#FF0000'
    ;;
esac
