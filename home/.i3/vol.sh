#!/bin/bash

ACTIVE_SINKS=$(pactl list sinks | grep -B2 RUNNING | grep "Sink #" | awk ' { print substr($NF, 2, length($NF)) } ')
CMD=$1

case $CMD in
    up)
        ADJ="+"
        ;;
    down)
        ADJ="-"
        ;;
    *)
        echo $"Usage: $0 {up|down}"
        exit 1
esac

for sink in $ACTIVE_SINKS; do
    CUR_VOLUME=$(pactl get-sink-volume $sink | awk '$1=="Volume:" { print substr($5, 0, length($5)-1) }')
    if [[ "$CUR_VOLUME" -lt 100 ]] || [[ "$ADJ" != "+" ]]; then
        pactl set-sink-volume $sink ${ADJ}1%
    fi
done
