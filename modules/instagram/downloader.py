from instaloader import instaloader, Post, ProfileNotExistsException, ConnectionException, ProfileHasNoPicsException, \
    BadResponseException
from utility.primary import getUserProfilePath


class Downloader:
    def __init__(self, target: str):
        self.target = target
        self.path = getUserProfilePath() + "/instagram/{target}"
        self.ig = instaloader.Instaloader(dirname_pattern=self.getStorePath())

    def getStorePath(self):
        return self.path.format(target=self.target)

    def downloadProfile(self):
        try:
            self.ig.download_profile(self.target, profile_pic_only=True)
            message = "Profile image was successfully downloaded.\nPath: {path}"
            return {
                "title": "Success",
                "message": message.format(path=self.getStorePath()),
                "status": 200
            }
        except ProfileNotExistsException as e:
            message = "Failed to download profile photo, reason: {reason}"
            message = message.format(reason=str(e))
            return {
                "title": "Error",
                "message": message,
                "status": 404
            }
        except ProfileHasNoPicsException:
            message = "This profile has no picture."
            return {
                "title": "Warning",
                "message": message,
                "status": 404
            }
        except ConnectionException as e:
            message = "Failed to connect, \nServer message: {server_message}"
            message = message.format(server_message=e)
            return {
                "title": "error",
                "message": message,
                "status": 500
            }
        except BadResponseException as e:
            message = "Unexpected error, \nServer message: {server_message}"
            message = message.format(server_message=e)
            return {
                "title": "error",
                "message": message,
                "status": 500
            }
        except:
            message = "Unexpected error."
            return {
                "title": "error",
                "message": message,
                "status": 0
            }

    def downloadPostPhoto(self):
        try:
            post = Post.from_shortcode(self.ig.context, self.target)
            self.ig.download_post(post, target="")
            message = "Post photo(s) was successfully downloaded.\nPath: {path}"
            return {
                "title": "Success",
                "message": message.format(path=self.getStorePath()),
                "status": 200
            }
        except ProfileNotExistsException as e:
            message = "Failed to download profile photo, reason: {reason}"
            message = message.format(reason=str(e))
            return {
                "title": "Error",
                "message": message,
                "status": 404
            }
        except ConnectionException as e:
            message = "Failed to connect, \nServer message: {server_message}"
            message = message.format(server_message=e)
            return {
                "title": "error",
                "message": message,
                "status": 500
            }
        except BadResponseException as e:
            message = "Unexpected error, \nServer message: {server_message}"
            message = message.format(server_message=e)
            return {
                "title": "error",
                "message": message,
                "status": 500
            }
        except Exception as e:
            message = "Unexpected error. detail: {detail}"
            message = message.format(detail=e)
            return {
                "title": "error",
                "message": message,
                "status": 0
            }
