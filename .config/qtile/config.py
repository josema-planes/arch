from os import path
import re
import socket
import subprocess
from libqtile import hook

from settings.keys import keys, mod
from settings.groups import groups
from settings.topbar import screens, widget_defaults, extension_defaults
from settings.layouts import layouts
from settings.path import qtile_path

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

bring_front_click = True
focus_on_window_activation = "focus"
