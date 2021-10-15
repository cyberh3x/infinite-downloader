from views.components.label.default import LabelComponent


class YoutubeView:
    def __init__(self, root):
        self.root = root

    def render(self):
        options = {
            "label": {
                "text": "Coming soon...!",
            },
            "grid": {
                "row": 0,
                "column": 0
            }
        }
        return LabelComponent(self.root, options).render()
