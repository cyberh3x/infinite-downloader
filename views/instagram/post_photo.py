from modules.instagram.downloader import Downloader as InstagramDownloaderModule
from views.components.input.default import TextFieldComponent
from views.components.label.default import LabelComponent
from views.components.button.default import ButtonComponent
from views.components.messageBox.default import PopupComponent


class PostPhoto:
    def __init__(self, root):
        self.root = root
        self.post_link_input = None

    def onSubmit(self):
        post_link = self.getPostLink()
        if post_link:
            module = InstagramDownloaderModule(post_link)
            response = module.downloadPostPhoto()
            title = response["title"]
            message = response["message"]
            code = response["code"]
            options = {}
            if code == 200:
                self.handleClearUsernameInput()
                options["type"] = None
            else:
                options["type"] = "error"
            PopupComponent(title, message, options).render()
        else:
            title = "Error"
            message = "Enter your post link"
            options = {
                "type": "error"
            }
            PopupComponent(title, message, options).render()

    def handleClearUsernameInput(self):
        self.post_link_input.delete(0, "end")

    def getPostLink(self):
        return self.post_link_input.get()

    def renderLabel(self):
        options = {
            "label": {
                "text": "Post link(Shortcode):",
            },
            "grid": {
                "row": 1,
                "column": 0
            }
        }
        return LabelComponent(self.root, options).render()

    def renderPostLinkInput(self):
        options = {
            "input": {
                "width": 59,
                "borderwidth": 5
            },
            "grid": {
                "column": 1,
                "row": 1,
                "columnspan": 3,
                "padx": 10,
                "pady": 10
            }
        }
        self.post_link_input = TextFieldComponent(self.root, options).render()
        return self.post_link_input

    def renderSubmitButton(self):
        options = {
            "button": {
                "text": "Download",
                "command": self.onSubmit
            },
            "grid": {
                "column": 0,
                "row": 3,
                "columnspan": 6,
                "padx": 10,
                "pady": 10
            }
        }
        return ButtonComponent(self.root, options).render()

    def render(self):
        self.renderPostLinkInput()
        self.renderLabel()
        self.renderSubmitButton()
