import subprocess
from os import path
from libqtile import hook

from libqtile import layout

from settings.keys import keys, mod
from settings.groups import groups
from settings.topbar import screens, widget_defaults, extension_defaults
from settings.layouts import layouts, floating_layout
from settings.path import qtile_path

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])


bring_front_click = True
focus_on_window_activation = "smart"