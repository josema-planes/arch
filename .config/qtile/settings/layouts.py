from libqtile import layout
from settings.colors import colors

layouts = [
    layout.MonadWide(
        margin = 6,
        border_focus = colors[4],
        borderwidth = 1,
    ),
    layout.MonadTall(
        margin = 6,
        border_focus = colors[4],
        borderwidth = 1,
    ),
    layout.Max(
        margin = 6,
    ),
    layout.Floating(),
]

# floating_layout = layout.Floating(float_rules=[])
