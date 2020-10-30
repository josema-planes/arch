from libqtile.config import Screen
from libqtile import bar, widget
import subprocess

colors = [
    "#FFFFFF", #white
    "#000000", #black
    "#9b9b9b", #grey
    "#FF0000", #red
    "#00FF00", #green
    "#0000FF", #blue
    ]

widget_defaults = dict(
    font="sans",
    fontsize = 18,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        ),
               widget.GroupBox(
                        fontsize = 18,
                        margin_y = 0, 
                        margin_x = 0, 
                        padding_y = 9, 
                        padding_x = 5, 
                        borderwidth = 4, 
                        active = colors[0], 
                        inactive = colors[2],
                        rounded = False,
                        highlight_method = "line",
                        this_current_screen_border = colors[3]
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        ),
                widget.WindowName(
                        fontsize = 14,
                        padding = 6
                        ),
                widget.Systray(),
                widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        ),
                widget.TextBox(
                        text="│", 
                        padding = 6,
                        fontsize=18
                        ),
                widget.TextBox(
                        text="⌂", 
                        padding = 6,
                        fontsize=18
                        ),
                widget.CurrentLayout(
                        fontsize=18,
                        ),
                widget.TextBox(
                        text="│", 
                        padding = 6,
                        fontsize=18
                        ),
                widget.TextBox(
                        text="☼",
                        padding = 6,
                        fontsize=22,
                        ),
                widget.Clock(
                        format="%A, %B %d - %H:%M",
                        fontsize=18,
                        ),
                widget.TextBox(
                        text="│", 
                        padding = 6,
                        fontsize=18
                        ),
                widget.TextBox(
                      text = "♪",
                       padding = 0,
                       fontsize=20,
                       ),
                widget.Volume(
                        padding = 5,
                        fontsize=18,
                        ),
                widget.TextBox(
                        text="│", 
                        padding = 6,
                        fontsize=18,
                        ),
                widget.TextBox(
                        text="↯",
                        fontsize=22,
                        padding = 0,
                        ),
                widget.Battery(
                        fontsize=18,
                        format='{percent:2.0%}',
                        ),
            ],
            24,
        ),
    ),
]
