from libqtile import layout
from settings.colors import colors

layout_style = {
    'margin': 8,
    'border_width': 1,
    'border_normal': colors["inactive"],
    'border_focus': colors["active"],
}

layouts = [
    layout.MonadWide(**layout_style),
    layout.MonadTall(**layout_style),
    layout.Max(),
    layout.Floating(),
]

floating_layout = layout.Floating(
    float_rules=[
        {"role": "EventDialog"},
        {"role": "Msgcompose"},
        {"role": "Preferences"},
        {"role": "pop-up"},
        {"role": "prefwindow"},
        {"role": "task_dialog"},
        {"wname": "Module"},
        {"wname": "Search Dialog"},
        {"wname": "Goto"},
        {"wname": "IDLE Preferences"},
        {"wname": "Create new database"},
        {"wname": "Preferences"},
        {"wname": "File Transfer"},
        {"wname": 'branchdialog'},
        {"wname": 'pinentry'},
        {"wname": 'confirm'},
        {"wmclass": 'dialog'},
        {"wmclass": 'download'},
        {"wmclass": 'error'},
        {"wmclass": 'file_progress'},
        {"wmclass": 'notification'},
        {"wmclass": 'splash'},
        {"wmclass": 'toolbar'},
        {"wmclass": 'confirmreset'},
        {"wmclass": 'yakuake'},
        {"wmclass": "GoldenDict"},
        {"wmclass": "Synapse"},
        {"wmclass": "Pamac-updater"},
        {"wmclass": "Galculator"},
        {"wmclass": "notify"},
        {"wmclass": "Nitrogen"},
        {"wmclass": 'ssh-askpass'},
        {"wmclass": "Mlconfig"},
        {"wmclass": "Alacritty"},
        {"wmclass": "Zoom"},
    ],
    border_focus = colors["active"]
)