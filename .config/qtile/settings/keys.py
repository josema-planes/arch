from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"
terminal = "alacritty"

keys = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod, 'shift'], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    
    # Launch GUI apps
    Key(
        [mod], "m", 
        lazy.spawn("firefox")
        ),
    Key(
        [mod], "c", 
        lazy.spawn("code")
        ),
    Key(
        [mod], "n", 
        lazy.spawn("nautilus")
        ),
    Key(
        [mod], "z", 
        lazy.spawn("zoom")
        ),
    Key(
        [mod], "v", 
        lazy.spawn("virtualbox")
        ),
    Key(
        [mod], "l", 
        lazy.spawn("libreoffice")
        ),
    Key(
        [mod], "d", 
        lazy.spawn("dmenu_run")
        ),

    # Volume
    Key(
        [], "XF86AudioRaiseVolume", 
        lazy.spawn("amixer set Master 5%+")
        ),
    Key(
        [], "XF86AudioLowerVolume", 
        lazy.spawn("amixer set Master 5%-")
        ),
    Key(
        [], "XF86AudioMute", 
        lazy.spawn("amixer set Master 0%")
        ),
    
    # Brightness
    Key(
        [], "XF86MonBrightnessUp", 
        lazy.spawn("brightnessctl set 10%+")
        ),
    Key(
        [], "XF86MonBrightnessDown", 
        lazy.spawn("brightnessctl set 10%-")
        ),
]
