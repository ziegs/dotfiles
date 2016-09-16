#!/bin/sh

xkbcomp -w0 -I$HOME/.xkb -R$HOME/.xkb keymap/mykbd $DISPLAY

trackpoint="TPPS/2 IBM TrackPoint"
touchpad="SynPS/2 Synaptics TouchPad"

# Enable vertical scrolling for TrackPoint
xinput set-prop "$trackpoint" "Evdev Wheel Emulation" 1
xinput set-prop "$trackpoint" "Evdev Wheel Emulation Button" 2
xinput set-prop "$trackpoint" "Evdev Wheel Emulation Timeout" 200

# Mouse sensitivity
xinput set-prop "$trackpoint" "Device Accel Constant Deceleration" 0.35
xinput set-prop "$touchpad" "Device Accel Constant Deceleration" 1.25

# Disable touchpad right click
synclient RightButtonAreaLeft=0
synclient RightButtonAreaTop=0

# Reverse scrolling
synclient VertTwoFingerScroll=1
synclient VertScrollDelta=-114
synclient HorizTwoFingerScroll=1
synclient HorizScrollDelta=-114

# Turn on palm detect (doesn't really work :/)
synclient PalmDetect=1

# Three finger click
synclient TapButton3=2

# Run syndaemon if it's not already running
sdpid=`ps -ef|grep -v grep|grep syndaemon|awk '{print $2}'`
if [ -z $sdpid ]
then
  echo "Starting syndaemon"
  syndaemon -i 1 -K -d
fi
