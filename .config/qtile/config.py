from libqtile import layout, hook

from settings.path import qtile_path
from settings.keys import mod, keys
from settings.layouts import layouts
from settings.groups import groups
from settings.topbar import screens

#---------------------
@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path)])

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'
