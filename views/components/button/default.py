from tkinter import Button


class ButtonComponent():
    def __init__(self, root, options: dict):
        self.root = root
        self.options = options

    def render(self):
        options = self.options
        button = Button(self.root, options["button"])
        button.grid(options["grid"])
        return button
