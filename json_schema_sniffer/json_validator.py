__all__ = ("JsonValidator",)

from pathlib import Path
from typing import Union
from exceptions import NotAFileError
from exceptions import InvalidJsonFileError


class JsonValidator:
    """Json validator class"""

    def __init__(self, json_path: Union[str, Path]) -> None:
        self.json_path = Path(json_path)

    def validate(self) -> None:
        """Carries out validation on the provided json file."""
        self.validate_path()
        self.validate_file_type()
        self.validate_extension()

    def validate_path(self) -> None:
        """Validates the path provided"""
        if not self.json_path.exists():
            raise FileNotFoundError(
                f"Invalid path specified: {self.json_path.as_posix()} "
                "does not exist on this file system."
            )

    def validate_file_type(self) -> None:
        """Validates the provided path is a valid file."""
        if not self.json_path.is_file():
            raise NotAFileError(f"The specified json file is not a valid file.")

    def validate_extension(self) -> None:
        """Validates the file extension, ensures a .json file is provided"""
        if not self.json_path.suffix == ".json":
            raise InvalidJsonFileError(
                f"Invalid file type specified: {self.json_path.as_posix()} "
                "is not a valid json file."
            )
