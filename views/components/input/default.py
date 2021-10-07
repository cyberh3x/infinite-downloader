from tkinter import Entry, StringVar


class TextFieldComponent():
    def __init__(self, root, text_field_options: dict, on_change=lambda x, y, a, b: {}):
        self.root = root
        self.options = text_field_options
        self.on_change = on_change

    def render(self):
        options = self.options
        string_var = StringVar()
        string_var.trace("w", lambda name, index, mode, sv=string_var: self.on_change(name, index, mode, sv))
        text_field = Entry(self.root, options["input"], textvariable=string_var)
        if "text" in options["input"]:
            text_field.insert(0, options["input"]["text"])
        text_field.grid(options["grid"])
        return text_field
