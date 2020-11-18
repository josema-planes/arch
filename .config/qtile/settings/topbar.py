from libqtile import bar, layout, widget
from libqtile.config import Screen

from settings.theme import colors

widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=24,
    padding=4,
    background = colors["bg"],
)

extension_defaults = widget_defaults.copy()


# Functions -------------------------------------------
def open_demenu(qtile):
    qtile.cmd_spawn('dmenu_run')

def shutdown(qtile):
    #qtile.cmd_to_layout_index(3)
    qtile.cmd_spawn('/home/josema/scripts/shutdown.py')

def settings(qtile):
    qtile.cmd_spawn('/home/josema/settings/settings.py')


def reload_qtile(qtile):
    qtile.cmd_simulate_keypress(["mod4", "shift"], "r")


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
                    margin_y = -1,
                    borderwidth = 2,
                    active = colors["active"],
                    inactive = colors["inactive"],
                    rounded = False,
                    highlight_method = "block",
                    this_current_screen_border = colors["focus"],
                    disable_drag=True,
                    ),

                widget.Prompt(),

                widget.Spacer(),

                powerline(colors["color4"], colors["bg"]),
                
                widget.CurrentLayoutIcon(
                    scale = 0.7,
                    background = colors["color4"],
                ),

                widget.CurrentLayout(
                    background = colors["color4"],
                ),

                powerline(colors["color2"], colors["color4"]),
                
                widget.TextBox(
                    text = "",
                    fontsize = 16,
                    background = colors["color2"],
                ),

                widget.Net(
                    interface = "wlo1",
                    format = '{down}↓{up}↑',
                    background = colors["color2"],
                    ),

                powerline(colors["color1"], colors["color2"]),

                widget.TextBox(
                    text = " ",
                    fontsize = 16,
                    background = colors["color1"],
                ),

                widget.Clock(
                    format = "%A, %B %d  [ %H:%M ]",
                    background = colors["color1"],
                    ),
            ],
            24,
        ),
        bottom=bar.Bar([
            
            widget.TextBox(
                    text = "",
                    fontsize = 38,
                    padding = 14,
                    mouse_callbacks = {'Button1': settings},
                ),

            widget.WindowName(
                    fontsize = 16,
                    padding = 18,
                    foreground = colors["active"],
                ),

            widget.Systray(
                    icon_size = 28,
                    padding = 8,
                ),

            widget.TextBox(
                text = "  ",
                fontsize = 18,
                mouse_callbacks = {'Button1': shutdown}
                ),
        ],
        30),
    ),
]