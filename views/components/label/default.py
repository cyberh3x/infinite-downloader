from tkinter import Label


class LabelComponent():
    def __init__(self, root, options: dict):
        self.root = root
        self.options = options

    def render(self):
        options = self.options
        label = Label(self.root, options["label"])
        label.grid(options["grid"])
        return label
