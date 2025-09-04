#!/bin/bash

playerctl -a pause

swaylock --indicator-idle-visible \
--indicator-radius 100 \
--daemonize \
--indicator-thickness 7 \
--line-uses-ring
