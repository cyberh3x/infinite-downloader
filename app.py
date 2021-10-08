from tkinter import *
from views.instagram.index import InstagramView
from views.layouts.footer import Footer


class App():
    def __init__(self):
        try:
            root = Tk()
            root.title("Instagram Downloader")
            root.iconbitmap("assets/images/icons/instagram.ico")
            root.geometry("500x230")
            self.renderInstagramViews(root)
            self.renderFooter(root)
            root.mainloop()
        except NameError as e:
            message = "Failed to run application, reason: {reason}"
            raise Exception(message.format(reason=str(e)))

    def renderInstagramViews(self, root):
        instagram_view = InstagramView(root)
        instagram_view.render()

    def renderFooter(self, root):
        footer_view = Footer(root)
        footer_view.render()


App()
