from pathlib import Path
from typing import Protocol, Any, Iterable, Union, Dict


class IJsonValidator(Protocol):
    def __init__(self, json_path: Union[str, Path]) -> None:
        ...

    def validate(self) -> None:
        ...

    def validate_path(self) -> None:
        ...

    def validate_file_type(self) -> None:
        ...

    def validate_extension(self) -> None:
        ...


class ISchemaStorage(Protocol):
    def save(
        self,
        file_name: str,
        data: Dict[str, Any],
        *args: Iterable[Any],
        **kwargs: Dict[str, Any]
    ) -> Union[str, Path]:
        ...
