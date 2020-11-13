import subprocess
from libqtile import hook

from settings.keys import keys, mod
from settings.groups import groups
from settings.topbar import screens, widget_defaults, extension_defaults
from settings.layouts import layouts, floating_layout
from settings.mouse import mouse
from settings.path import qtile_path


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])
