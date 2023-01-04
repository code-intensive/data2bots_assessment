import json
from pathlib import Path
from typing import Any, Dict, Iterable, Union


class LocalJsonFileStorage:
    def save(
        self,
        file_name: str,
        data: Dict[str, Any],
        *args: Iterable[Any],
        **kwargs: Dict[str, Any],
    ) -> Union[str, Path]:
        base_path = kwargs.pop("base_path", ".")
        file_path = Path(base_path).joinpath(f"{file_name}.json")  # type:ignore
        json_data = json.dumps(data)
        with open(file_path, "a") as sniffed_schema:
            sniffed_schema.write(json_data)
        return file_path.as_posix()
