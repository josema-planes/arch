import json

theme_path = "/home/josema/.config/qtile/themes/material-ocean.json"

# Set theme acording to path
with open(theme_path) as f:
    data = json.load(f)

colors = (data)