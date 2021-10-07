from modules.instagram.downloader import Downloader as InstagramDownloaderModule
from views.components.input.default import TextFieldComponent
from views.components.label.default import LabelComponent
from views.components.button.default import ButtonComponent
from views.components.messageBox.default import PopupComponent
from tkinter.filedialog import askdirectory


class InstagramView():
    def __init__(self, root):
        self.root = root
        self.username_input = None
        self.save_to_input = None

    def onSubmit(self):
        path_to_save = self.getSaveToPath()
        username = self.getUsername()
        if username:
            module = InstagramDownloaderModule(username, path_to_save)
            response = module.downloadProfile()
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
            message = "Enter your username"
            options = {
                "type": "error"
            }
            PopupComponent(title, message, options).render()

    def onBrowseClick(self):
        self.handleClearSaveToInput()
        self.save_to_input.insert(0, askdirectory())

    def handleClearSaveToInput(self):
        self.save_to_input.delete(0, 'end')

    def handleClearUsernameInput(self):
        self.username_input.delete(0, "end")

    def getUsername(self):
        return self.username_input.get()

    def getSaveToPath(self):
        return self.save_to_input.get()

    def renderLabel(self):
        options = {
            "label": {
                "text": "Username:",
            },
            "grid": {
                "row": 0,
                "column": 0
            }
        }
        return LabelComponent(self.root, options).render()

    def renderUsernameInput(self):
        options = {
            "input": {
                "width": 69,
                "borderwidth": 5
            },
            "grid": {
                "column": 1,
                "row": 0,
                "columnspan": 3,
                "padx": 10,
                "pady": 10
            }
        }
        self.username_input = TextFieldComponent(self.root, options).render()
        return self.username_input

    def renderSaveToInputLabel(self):
        options = {
            "label": {
                "text": "Save to",
            },
            "grid": {
                "row": 1,
                "column": 0
            }
        }
        return LabelComponent(self.root, options).render()

    def renderSaveToInput(self):
        options = {
            "input": {
                "width": 40,
                "borderwidth": 5
            },
            "grid": {
                "column": 1,
                "row": 1,
                "pady": 10
            }
        }
        self.save_to_input = TextFieldComponent(self.root, options).render()
        return self.save_to_input

    def renderBrowseAskDirectoryButton(self):
        options = {
            "button": {
                "text": "Browse",
                "command": self.onBrowseClick
            },
            "grid": {
                "column": 2,
                "row": 1,
                "padx": 10,
                "pady": 10
            }
        }
        return ButtonComponent(self.root, options).render()

    def renderSubmitButton(self):
        options = {
            "button": {
                "text": "Download",
                "command": self.onSubmit
            },
            "grid": {
                "column": 0,
                "row": 2,
                "columnspan": 6,
                "padx": 10,
                "pady": 10
            }
        }
        return ButtonComponent(self.root, options).render()

    def render(self):
        self.renderUsernameInput()
        self.renderLabel()
        self.renderSaveToInputLabel()
        self.renderSaveToInput()
        self.renderBrowseAskDirectoryButton()
        self.renderSubmitButton()
