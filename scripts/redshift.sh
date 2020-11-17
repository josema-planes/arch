#!/bin/bash

# Set night light acording to location
redshift -x

redshift -O 3400

notify-send "Night light mode on"
