#!/bin/bash

# Set night light acording to location
redshift -l 37.98704:-1.13004 &

notify-send "Night light mode on"
