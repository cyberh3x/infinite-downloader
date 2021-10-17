from tkinter import messagebox


class PopupComponent:
    def __init__(self, title, message, options=None):
        if options is None:
            options = {}
        self.title = title
        self.message = message
        self.options = options

    def render(self):
        options = self.options
        label = None
        if "type" in options:
            type = options['type']
            if type is None:
                label = messagebox.showinfo(self.title, self.message)
            elif type == "error":
                label = messagebox.showerror(self.title, self.message)
            else:
                label = messagebox.showwarning(self.title, self.message)
        return label
