from youtube_dl import YoutubeDL
from utility.primary import getUserProfilePath


class Downloader:
    def __init__(self, url: str, options: dict = None):
        self.path_prefix = getUserProfilePath() + "/youtube"
        default_options = {
            "outtmpl": self.path_prefix + "/%(id)s - %(title)s - %(format)s.%(ext)s"
        }
        if options is None:
            options = {}
        options.update(default_options)
        self.options = options
        self.url = url
        self.ydl = YoutubeDL(options)

    def downloadVideo(self):
        try:
            urls = self.url.split(",")
            self.ydl.download(urls)
            message = "Video was successfully downloaded.\nPath: {path}"
            return {
                "title": "Success",
                "message": message.format(path=self.path_prefix),
                "status": 200
            }
        except Exception as e:
            message = "Error in downloading video, reason: {reason}"
            return {
                "title": "Error",
                "message": message.format(reason=e),
                "status": 0
            }
