#!/bin/sh

xkbcomp -w0 -I$HOME/.xkb -R$HOME/.xkb keymap/mykbd $DISPLAY

trackpoint="TPPS/2 IBM TrackPoint"
touchpad="SynPS/2 Synaptics TouchPad"

xinput set-prop "$touchpad" "libinput Natural Scrolling Enabled" 1 # correct scrolling direction
xinput set-prop "$touchpad" "libinput Tapping Enabled" 1 # tap-to-click
xinput set-prop "$touchpad" "libinput Click Method Enabled" 0, 1 # two-finger right click
xinput set-prop "$touchpad" "libinput Accel Speed" 1.0 # fastest, doesn't feel as fast as I want it, figuring it out
