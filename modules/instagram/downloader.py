from instaloader import instaloader, ProfileNotExistsException, ConnectionException, ProfileHasNoPicsException, \
    BadResponseException
from utility.primary import getUserProfilePath


class Downloader():
    def __init__(self, username: str, path_to_save: str):
        self.username = username
        if path_to_save:
            self.path_to_save = path_to_save
        else:
            self.path_to_save = getUserProfilePath()
        self.path_to_save += "/{username}"
        self.ig = instaloader.Instaloader(dirname_pattern=self.getStorePath())

    def getStorePath(self):
        return self.path_to_save.format(username=self.username)

    def downloadProfile(self):
        try:
            self.ig.download_profile(self.username, profile_pic_only=True)
            message = "Profile image was successfully downloaded."
            return {
                "title": "Success",
                "message": message,
                "code": 200
            }
        except ProfileNotExistsException as e:
            message = "Failed to download profile photo, reason: {reason}"
            message = message.format(reason=str(e))
            return {
                "title": "Error",
                "message": message,
                "code": 404
            }
        except ProfileHasNoPicsException:
            message = "This profile has no picture."
            return {
                "title": "Warning",
                "message": message,
                "code": 404
            }
        except ConnectionException as e:
            message = "Failed to connect, \nServer message: {server_message}"
            message = message.format(server_message=e)
            return {
                "title": "error",
                "message": message,
                "code": 500
            }
        except BadResponseException as e:
            message = "Unexpected error, \nServer message: {server_message}"
            message = message.format(server_message=e)
            return {
                "title": "error",
                "message": message,
                "code": 500
            }
        except:
            message = "Unexpected error."
            return {
                "title": "error",
                "message": message,
                "code": 0
            }
