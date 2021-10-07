import os


def getUserProfilePath(suffix: str = "OneDrive\\Pictures\\Instagram Downloader"):
    return os.path.expanduser(os.sep.join(["~", suffix]))
