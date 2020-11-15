from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "alacritty"

keys = [
    # Change focused window
    Key([mod], "Tab",  lazy.layout.next()),

    #-----------------------------------------------------
    Key([mod, "shift"], "q", lazy.window.kill()), # Kill actual window

    Key([mod, "shift"], "r", lazy.restart()), # Restart qtile

    Key([mod], "r", lazy.spawncmd()), # Open promp in bar
    #------------------------------------------------------

    # Launch programs
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "m", lazy.spawn("firefox")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "d", lazy.spawn("dmenu_run")),
    Key([mod], "n", lazy.spawn("thunar")),
    Key([mod], "v", lazy.spawn("virtualbox")),
    Key([mod], "l", lazy.spawn("libreoffice")),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("/home/josema/scripts/volume.sh down")),
    Key([],"XF86AudioRaiseVolume", lazy.spawn("/home/josema/scripts/volume.sh up")),
    Key([],"XF86AudioMute", lazy.spawn("amixer set Master 0%")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("/home/josema/scripts/brightness.sh up")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("/home/josema/scripts/brightness.sh down")),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot /home/josema/images/screen_shot")),
]
