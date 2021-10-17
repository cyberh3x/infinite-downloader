from views.youtube.video import Video


class YoutubeView:
    def __init__(self, root):
        self.root = root

    def render(self):
        Video(self.root).render()
