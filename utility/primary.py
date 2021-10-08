import os


def getUserProfilePath(suffix: str = "Pictures\\Instagram-Downloader"):
    return os.path.expanduser(os.sep.join(["~", suffix]))
