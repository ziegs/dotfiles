#!/bin/sh

#(sleep 2; nm-applet) &
(sleep 2; killall orca) &
(sleep 2; /usr/share/goobuntu-indicator/goobuntu_indicator.py) &
(sleep 2; gsettings-data-convert) &
(sleep 2; start-pulseaudio-x11) &
