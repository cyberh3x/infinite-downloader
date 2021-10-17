import os


def getUserProfilePath(suffix: str = "Infinite-Downloader"):
    return os.path.expanduser(os.sep.join(["~", suffix]))
