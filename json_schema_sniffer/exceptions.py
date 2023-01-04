class NotAFileError(OSError):
    """Error if provided path is not a File"""

    pass


class InvalidJsonFileError(OSError):
    """Error when File provided does not end with a .json extension"""
