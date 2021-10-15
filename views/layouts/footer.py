from views.components.label.default import LabelComponent


class Footer():
    def __init__(self, root):
        self.root = root
        self.email = "sajjad.n18@outlook.com"
        self.message = "Developed by Sajjad Noori"

    def renderDeveloperLabel(self):
        options = {
            "label": {
                "text": self.message,
            },
            "grid": {
                "row": 4,
                "columnspan": 6,
                "column": 0
            }
        }
        return LabelComponent(self.root, options).render()

    def renderEmailLabel(self):
        options = {
            "label": {
                "text": "Email: " + self.email,
            },
            "grid": {
                "row": 5,
                "columnspan": 6,
                "column": 0,
            }
        }
        return LabelComponent(self.root, options).render()

    def render(self):
        self.renderDeveloperLabel()
        self.renderEmailLabel()
