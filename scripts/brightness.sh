#!/bin/bash

# You can call this script like this:
# $./brightness.sh up
# $./brightness.sh down

function get_brightness {
    brightnessctl | cut -d ' ' -f 4 | grep -o '[0-9]*'
}

function send_notification {
    brightness=`get_brightness`
    # Make the bar with the special character ─ (it's not dash -)
    bar=$(seq -s "─" $(($brightness / 5)) | sed 's/[0-9]//g')
    # Send the notification
    dunstify -r 2593 -u normal "  $bar  ""$brightness"
}

case $1 in
    up)
	# Increases brighness (+ 10%)
	brightnessctl set 10%+
	send_notification
	;;
    down)
    # Decresase brightness (- 10%)
	brightnessctl set 10%-
	send_notification
	;;
esac
