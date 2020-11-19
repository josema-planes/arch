import json
import os
from os import path

from settings.path import qtile_path


def load_theme():
    # If file exist load it
    try:
        config_file = path.join(qtile_path, "config.json")
        if path.isfile(config_file):
            with open(config_file) as f:
                myTheme = json.load(f)["theme"]

        theme_path = path.join(qtile_path, "themes", f"{myTheme}.json")

        with open(theme_path) as f:

            if(myTheme != "material-ocean"):
                os.system("notify-send 'Theme has changed'")
            
            return json.load(f)

    except:
        os.system("notify-send 'There was a problem at trying to change theme'")

        theme_path = "/home/josema/.config/qtile/themes/material-ocean.json"
        
        with open(theme_path) as f:
            return json.load(f)


colors = load_theme()