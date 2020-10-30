from libqtile.config import Key, Group
from libqtile.command import lazy
from settings.keys import mod, keys

group_names = ["TERM","WWW","CODE","DOC","ZOOM","WORK"]

groups = [Group(name) for name in group_names]

for i, (name) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group       
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))
