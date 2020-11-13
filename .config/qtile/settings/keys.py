from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "alacritty"

keys = [
    Key([mod, "shift"], "q", lazy.window.kill()), # Kill actual window

    Key([mod, "shift"], "r", lazy.restart()), # Restart qtile

    Key([mod], "r", lazy.spawncmd()), # Open promp in bar

    # Launch programs
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "m", lazy.spawn("firefox")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "d", lazy.spawn("dmenu_run")),
    Key([mod], "n", lazy.spawn("nautilus")),
    Key([mod], "v", lazy.spawn("virtualbox")),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master 0%")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]
