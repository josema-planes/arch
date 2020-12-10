from os import path
import subprocess
import json


def load_theme():

    qtile_path = path.join(path.expanduser('~'), ".config" "/qtile")
    config = path.join(qtile_path, "theme.json")

    with open(config) as f:
        theme = json.load(f)["theme"]

    theme_file = path.join(qtile_path, "themes", f'{theme}.json')
    if not path.isfile(theme_file):
        raise Exception(f'"{theme_file}" does not exist')

    with open(path.join(theme_file)) as f:
        return json.load(f)


colors = load_theme()