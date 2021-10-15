from views.components.tab.default import TabComponent
from views.instagram.profile_photo import ProfilePhoto
from views.instagram.post_photo import PostPhoto
from config.constant import INSTAGRAM_POST_PHOTO_KEY, INSTAGRAM_PROFILE_PHOTO_KEY

class InstagramView:
    def __init__(self, root):
        self.root = root

    def renderTabs(self):
        options = {
            "grid": {
                "row": 1,
                "column": 0,
                "pady": 10
            }
        }
        tabs = [
            {
                "label": "Profile photo",
                "key": INSTAGRAM_PROFILE_PHOTO_KEY
            },
            {
                "label": "Post image",
                "key": INSTAGRAM_POST_PHOTO_KEY
            },
        ]
        tabs = TabComponent(self.root, tabs, options).render()
        ProfilePhoto(tabs[INSTAGRAM_PROFILE_PHOTO_KEY]).render()
        PostPhoto(tabs[INSTAGRAM_POST_PHOTO_KEY]).render()
        return tabs

    def render(self):
        self.renderTabs()
