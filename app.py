from tkinter import *
from views.components.tab.default import TabComponent
from views.instagram.index import InstagramView
from views.youtube.index import YoutubeView
from views.layouts.footer import Footer
from config.constant import INSTAGRAM_KEY, YOUTUBE_KEY


class App:
    def __init__(self):
        try:
            root = Tk()
            root.title("Infinite Downloader")
            root.iconbitmap("assets/images/icons/app.ico")
            root.geometry("500x235")
            self.renderTabs(root)
            self.renderFooter(root)
            root.mainloop()
        except NameError as e:
            message = "Failed to run application, reason: {reason}"
            raise Exception(message.format(reason=str(e)))

    def renderTabs(self, root):
        options = {
            "grid": {
                "row": 0,
                "column": 0
            }
        }
        tabs = [
            {
                "label": "Instagram",
                "key": INSTAGRAM_KEY
            },
            {
                "label": "Youtube",
                "key": YOUTUBE_KEY
            },
        ]
        tabs = TabComponent(root, tabs, options).render()
        self.renderInstagramView(tabs[INSTAGRAM_KEY]).render()
        self.renderYoutubeView(tabs[YOUTUBE_KEY]).render()
        return tabs

    def renderInstagramView(self, root):
        instagram_view = InstagramView(root)
        return instagram_view

    def renderYoutubeView(self, root):
        youtube_view = YoutubeView(root)
        return youtube_view

    def renderFooter(self, root):
        footer_view = Footer(root)
        footer_view.render()


App()
