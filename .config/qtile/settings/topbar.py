from libqtile import bar, layout, widget
from libqtile.config import Screen

widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=24,
    padding=4,
)
extension_defaults = widget_defaults.copy()

# Functions
def open_demenu(qtile):
    qtile.cmd_spawn('nautilus')
    qtile.cmd_spawn('firefox')

def run_redshift(qtile):
    qtile.cmd_spawn('/home/josema/scripts/redshift.sh')


# Widgets
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize = 45,
                    padding_y = 5,
                    padding = 10,
                    borderwidth = 3,
                    active = "#FFFFFF",
                    rounded = False,
                    highlight_method = "block",
                    this_current_screen_border = "#AA4444",
                    disable_drag=True
                    ),

                widget.Prompt(),

                widget.WindowName(
                    fontsize = 14,
                    foreground = "#a151d3",
                    ),

                 widget.TextBox(
                    text=" ",
                    fontsize=37,
                    padding=-2,
                    background = "#000000",
                    foreground = "#fb9f7f",
                    ),

                widget.CurrentLayout(
                    background = "#fb9f7f",
                ),

                widget.TextBox(
                    text=" ",
                    fontsize=37,
                    padding=-2,
                    background = "#fb9f7f",
                    foreground = "#F07178",
                    ),
                
                widget.TextBox(
                    text = "",
                    fontsize = 16,
                    background = "#F07178",
                ),

                widget.Net(
                    interface = "wlo1",
                    format = '{down}↓{up}↑',
                    background = "#F07178",
                    ),

                widget.TextBox(
                    text=" ",
                    fontsize=37,
                    padding=-2,
                    background = "F07178",
                    foreground = "#a151d3",
                    ),

                widget.TextBox(
                    text = " ",
                    fontsize = 16,
                    background = "#a151d3",
                ),

                widget.Clock(
                    format = '%I:%M %p',
                    background = "#a151d3",
                    ),

                #widget.TextBox(text = "| ♪"),
                #widget.Volume(),

                #widget.TextBox(
                #    text = "| ",
                #    fontsize = 16
                #    ),

                #widget.Battery(
                #    format = '{char} {percent:2.0%}',
                #    charge_char = "⚡",
                #    discharge_char = " ",
                #    notify_below = 20,
                #    low_foreground = 'FF0000',
                #    low_percentage = 0.3,
                #    update_interval = 30,
                #    ),

                widget.TextBox(
                    text=" ",
                    fontsize=37,
                    padding=-2,
                    background = "#a151d3",
                    foreground = "#000000",
                    ),

                widget.TextBox(
                    text = "1",
                    mouse_callbacks = {'Button1': open_demenu},
                ),
                
                widget.TextBox(
                    text = "☽",
                    mouse_callbacks = {'Button1': run_redshift},
                ),
                
                widget.Systray(
                    icon_size = 24,
                    padding = 8,
                ),
            ],
            24,
        ),
    ),
]
