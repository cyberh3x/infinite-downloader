from tkinter import Radiobutton, IntVar


class RadioButtonComponent:
    def __init__(self, root, options: dict):
        self.root = root
        self.options = options

    def render(self):
        options = self.options
        var = IntVar()
        radio_button = Radiobutton(self.root, options["radio"])
        radio_button.grid(options["grid"])
        return radio_button, var
