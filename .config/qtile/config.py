from libqtile import hook

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

import subprocess

mod = "mod4"
terminal = "alacritty"

#=============================================================================================
colors=[
    "#292d3e",

    "#f1ffff",
    "#4c566a",
    "#ff5555",

    "#a151d3",
    "#f07178",
    "#fb9f7f",
    "#ffd47e"
]

#=============================================================================================
keys = [
    # Change focused window
    Key([mod], "Tab",  lazy.layout.next()),

    #-----------------------------------------------------
    Key([mod, "shift"], "q", lazy.window.kill()), # Kill actual window

    Key([mod, "shift"], "r", lazy.restart()), # Restart qtile
    
    Key([mod, "shift"], "Escape", lazy.shutdown()), # Log off qtile

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
    Key([], "XF86AudioLowerVolume", lazy.spawn("changeVolume 5%-")),
    Key([],"XF86AudioRaiseVolume", lazy.spawn("changeVolume 5%+")),
    Key([],"XF86AudioMute", lazy.spawn("changeVolume toggle")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("changeBrightness 10%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("changeBrightness 10%-")),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot /home/josema/images/screen_shot")),
]

#=============================================================================================
groups = [Group(i) for i in [
    "  ", "  ", "  ", "  ", "  ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

#=============================================================================================
layout_style = {
    'margin': 4,
    'border_width': 1,
    'border_normal': colors[1],
    'border_focus': colors[2],
}

layouts = [
    layout.MonadTall(**layout_style),
]

#=============================================================================================
widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=18,
    padding=4,
    background = colors[0],
)

extension_defaults = widget_defaults.copy()


# Widgets types -------------------------------------------

def powerline(myFg, myBg):
    return widget.TextBox(
        text = " ",
        fontsize = 37,
        padding = -2,
        foreground = myFg,
        background = myBg
        )


# Widgets --------------------------------------------------

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize = 35,
                    padding = 10,
                    borderwidth = 2,
                    active = colors[1],
                    inactive = colors[2],
                    rounded = False,
                    highlight_method = "block",
                    this_current_screen_border = colors[3],
                    disable_drag=True,
                    ),

                widget.Prompt(),

                widget.WindowName(
                    fontsize = 12,
                    padding = 18,
                    foreground = colors[1],
                ),

                widget.Spacer(),

                powerline(colors[7], colors[0]),
                
                widget.CurrentLayoutIcon(
                    scale = 0.7,
                    background = colors[7],
                ),

                widget.CurrentLayout(
                    background = colors[7],
                ),

                powerline(colors[5], colors[7]),
                
                widget.TextBox(
                    text = "",
                    fontsize = 16,
                    background = colors[5],
                ),

                widget.Net(
                    interface = "wlo1",
                    format = '{down}↓{up}↑',
                    background = colors[5],
                    ),

                powerline(colors[4], colors[5]),

                widget.TextBox(
                    text = " ",
                    fontsize = 16,
                    background = colors[4],
                ),

                widget.Clock(
                    format = "%A, %B %d  [ %H:%M ]",
                    background = colors[4],
                    ),
                
                powerline(colors[0], colors[4]),
                
                widget.Systray(
                    icon_size = 28,
                    padding = 8,
                ),
            ],
            24,
        ),
    ),
]

#=============================================================================================
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#=============================================================================================
@hook.subscribe.startup_once
def autostart():
    subprocess.call("/home/josema/.config/qtile/autostart.sh")


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry

    {'wname': 'zoom'},
    {'wmclass': 'zoom'},
])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"