from modules.youtube.downloader import Downloader
from views.components.label.default import LabelComponent
from views.components.input.default import TextFieldComponent
from views.components.button.default import ButtonComponent
from views.components.messageBox.default import PopupComponent
from views.components.radioButton.default import RadioButtonComponent
from tkinter import IntVar


class Video:
    def __init__(self, root):
        self.root = root
        self.video_url_input = None
        self.var = None
        self.low_quality_radio_buttons = None
        self.high_quality_radio_buttons = None

    def getUrlInputValue(self):
        return self.video_url_input.get()

    def getQuality(self):
        return self.var.get()

    def handleClearUrlInput(self):
        self.video_url_input.delete(0, "end")

    def onSubmit(self):
        url = self.getUrlInputValue()
        if url:
            quality = "worst" if self.getQuality() == 0 else "best"
            options = {
                'format': quality,
            }
            response = Downloader(url, options).downloadVideo()
            title = response["title"]
            message = response["message"]
            status = response["status"]
            options = {}
            if status == 200:
                self.handleClearUrlInput()
                options["type"] = None
            else:
                options["type"] = "error"
            PopupComponent(title, message, options).render()
        else:
            title = "Error"
            message = "Enter your video URL"
            options = {
                "type": "error"
            }
            PopupComponent(title, message, options).render()

    def renderUrlInputLabel(self):
        options = {
            "label": {
                "text": "Video URL:",
            },
            "grid": {
                "row": 0,
                "column": 1
            }
        }
        return LabelComponent(self.root, options).render()

    def renderVideoUrlInput(self):
        options = {
            "input": {
                "width": 64,
                "borderwidth": 5
            },
            "grid": {
                "column": 2,
                "row": 0,
                "padx": 10,
                "pady": 10
            }
        }
        self.video_url_input = TextFieldComponent(self.root, options).render()
        return self.video_url_input

    def renderQualityLabel(self):
        options = {
            "label": {
                "text": "Quality:",
            },
            "grid": {
                "row": 1,
                "column": 1
            }
        }
        return LabelComponent(self.root, options).render()

    def renderQualityRadioButtons(self):
        self.var = IntVar()
        low_options = {
            "radio": {
                "text": "Low",
                "value": 0,
                "variable": self.var
            },
            "grid": {
                "column": 1,
                "row": 2,
                "pady": 10
            }
        }
        high_options = {
            "radio": {
                "text": "High",
                "value": 1,
                "variable": self.var
            },
            "grid": {
                "column": 2,
                "row": 2,
                "pady": 10
            }
        }
        self.low_quality_radio_buttons = RadioButtonComponent(self.root, low_options).render()
        self.high_quality_radio_buttons = RadioButtonComponent(self.root, high_options).render()
        return True

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
        self.renderUrlInputLabel()
        self.renderVideoUrlInput()
        self.renderQualityLabel()
        self.renderQualityRadioButtons()
        self.renderSubmitButton()
