#!/bin/bash

state=`synclient -l | fgrep TouchpadOff | sed 's/^.*= //'`
if [ $state -eq 1 ]
then
        synclient TouchpadOff=0
else
        synclient TouchpadOff=1
fi

