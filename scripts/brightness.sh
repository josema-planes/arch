#!/bin/bash

# You can call this script like this:
# $./brightnes.sh up
# $./brightnes.sh down

function getProgressString {
    ITEMS="$1" # The total number of items(the width of the bar)
    FILLED_ITEM="$2" # The look of a filled item 
    NOT_FILLED_ITEM="$3" # The look of a not filled item
    STATUS="$4" # The current progress status in percent

    # calculate how many items need to be filled and not filled
    FILLED_ITEMS=$(echo "((${ITEMS} * ${STATUS})/100 + 0.5) / 1" | bc)
    NOT_FILLED_ITEMS=$(echo "$ITEMS - $FILLED_ITEMS" | bc)

    # Assemble the bar string
    msg=$(printf "%${FILLED_ITEMS}s" | sed "s| |${FILLED_ITEM}|g")
    msg=${msg}$(printf "%${NOT_FILLED_ITEMS}s" | sed "s| |${NOT_FILLED_ITEM}|g")
    echo "$msg"
}

function get_brightness {
    brightnessctl i | grep -o [0-9]*% | cut -d '%' -f 1
}

function send_notification {
    brightness=`get_brightness`

    # Make the bar with the special character ─ (it's not dash -)
    dunstify -r 2593 -a "changeBrightness" -u low \
    "Brightness: ${brightness}%" "$(getProgressString 10 "<b>─</b>" "─" $brightness)"
}

case $1 in
    up)
	# Increases brightness (+ 10%)
	brightnessctl set 10%+ > /dev/null
	send_notification
	;;
    down)
    # Decreases brightness (- 10%)
	brightnessctl set 10%- > /dev/null
	send_notification
	;;
esac
