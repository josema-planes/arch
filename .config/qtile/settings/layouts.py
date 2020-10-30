from libqtile import layout

colors = [
    "#FFFFFF", #white
    "#000000", #black
    "#9b9b9b", #grey
    "#FF0000", #red
    "#00FF00", #green
    "#0000FF", #blue
    ]

layouts = [
    layout.MonadTall(
        border_width = 3,
        border_focus = colors[0],
        margin = 12
        ),
    layout.Floating(
        float_rules=[dict(wmclass="zoom")],
        border_focus = colors[0],
        margin = 12
        )
    ]
