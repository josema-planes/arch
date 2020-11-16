from libqtile import bar, layout, widget
from libqtile.config import Screen

from settings.colors import colors

widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=24,
    padding=4,
    background = colors[7],
)

extension_defaults = widget_defaults.copy()

# Functions -------------------------------------------
def open_demenu(qtile):
    qtile.cmd_spawn('dmenu_run')

def run_redshift(qtile):
    qtile.cmd_spawn('/home/josema/scripts/redshift.sh')

def shutdown(qtile):
    qtile.cmd_to_layout_index(3)
    qtile.cmd_spawn('/home/josema/scripts/shutdown.py')

def reload_qtile(qtile):
    qtile.cmd_simulate_keypress(["mod4", "shift"], "r")


# Widgets -------------------------------------------
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize = 35,
                    padding = 10,
                    margin_y = -1,
                    borderwidth = 2,
                    active = colors[4],
                    inactive = colors[5],
                    rounded = False,
                    highlight_method = "block",
                    this_current_screen_border = colors[6],
                    disable_drag=True,
                    ),

                widget.Prompt(),

                widget.Spacer(),

                 widget.TextBox(
                    text=" ",
                    fontsize=37,
                    padding=-2,
                    background =  colors[7],
                    foreground = colors[2],
                    ),
                
                widget.CurrentLayoutIcon(
                    scale = 0.7,
                    background = colors[2],
                ),

                widget.CurrentLayout(
                    background = colors[2],
                ),

                widget.TextBox(
                    text=" ",
                    fontsize=37,
                    padding=-2,
                    background = colors[2],
                    foreground = colors[1],
                    ),
                
                widget.TextBox(
                    text = "",
                    fontsize = 16,
                    background = colors[1],
                ),

                widget.Net(
                    interface = "wlo1",
                    format = '{down}↓{up}↑',
                    background = colors[1],
                    ),

                widget.TextBox(
                    text=" ",
                    fontsize=37,
                    padding=-2,
                    background = colors[1],
                    foreground = colors[0],
                    ),

                widget.TextBox(
                    text = " ",
                    fontsize = 16,
                    background = colors[0],
                ),

                widget.Clock(
                    format = "%A, %B %d  [ %H:%M ]",
                    background = colors[0],
                    ),
            ],
            24,
        ),
        bottom=bar.Bar([

            widget.WindowName(
                    fontsize = 16,
                    foreground = colors[4],
                    ),
            
            widget.TextBox(
                text = "  ",
                fontsize = 18,
                mouse_callbacks = {'Button1': run_redshift}
            ),

            widget.Systray(
                    icon_size = 28,
                    padding = 8,
                ),

                widget.TextBox(
                    text = "  ",
                    fontsize = 16,
                    mouse_callbacks = {'Button1': shutdown},
                ),
        ],
        30),
    ),
]
