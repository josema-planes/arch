#!/bin/bash

# You can call this script like this:
# $./volume.sh up
# $./volume.sh down

function get_volume {
    amixer get Master | grep -o [0-9]*% | cut -d '%' -f 1
}

function send_notification {
    volume=`get_volume`
    # Make the bar with the special character ─ (it's not dash -)
    bar=$(seq -s "─" $(($volume / 5)) | sed 's/[0-9]//g')
    # Send the notification
    dunstify -r 2593 -u normal "  $bar  ""$volume"
}

case $1 in
    up)
	# Increases volume (+ 5%)
	amixer set Master 5%+
	send_notification
	;;
    down)
    # Decreases volume (- 5%)
	amixer set Master 5%-
	send_notification
	;;
esac
