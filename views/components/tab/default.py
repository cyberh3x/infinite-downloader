from tkinter import ttk
from tkinter import BOTH, TRUE


class TabComponent:
    def __init__(self, root, tab_list: dict, options: dict):
        self.root = root
        self.tab_list = tab_list
        self.options = options

    def render(self):
        options = self.options
        tabs = ttk.Notebook(self.root)
        tabs.grid(options["grid"])
        tab_list = self.tab_list
        frames = {}
        for item in tab_list:
            frame = ttk.Frame(tabs)
            label = item["label"]
            tabs.add(frame, text=label)
            key = item["key"]
            frames[key] = frame
        return frames
