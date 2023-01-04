import json
from pprint import pprint
from typing import Any, Iterable, Dict, List, Collection, Union
from pathlib import Path
from protocols import IJsonValidator, ISchemaStorage


class SchemaSniffer:
    PREVIEW_INDENTS = 2
    TYPES = {"str": "string"}

    def __init__(
        self, *, json_path: str, validator: IJsonValidator, storage: ISchemaStorage
    ):
        self.storage = storage()
        self.validator = validator(json_path)

        self.validator.validate()
        self._schema_path = Path(json_path).as_posix()
        self._data: Dict[Any, Any] = SchemaSniffer._load_json(self._schema_path)
        self._sniffed_schema: Union[Collection[Any], None] = None

    @staticmethod
    def _load_json(json_path: str) -> Dict[Any, Any]:
        with open(json_path, "r") as json_file:
            data = json_file.read()
        return json.loads(data)

    def preview_data(self) -> None:
        pprint(self._data, indent=self.PREVIEW_INDENTS)

    def retrieve_data(self) -> Dict[str, Any]:
        return self._data

    def preview_schema(self) -> None:
        if self.sniffed_schema_exists:
            pprint(self._sniffed_schema, indent=self.PREVIEW_INDENTS)

    def retrieve_schema(self) -> Union[Collection[Any], None]:
        if self.sniffed_schema_exists:
            return self._sniffed_schema
        return None

    def sniff_schema(self) -> None:
        self.__sniff_schema__()

    def save(self, file_name: str, *args: Iterable[Any], **kwargs: Dict[str, Any]) -> Any:
        return self.storage.save(file_name, self._sniffed_schema, *args, **kwargs) # type:ignore

    def _get_type(self, key: Any) -> str:
        if isinstance(key, str):
            return "string"
        if isinstance(key, int):
            return "int"
        if isinstance(key, list):
            return "enum"
        if isinstance(key, dict):
            return "array"
        if isinstance(key, bool):
            return "boolean"
        return "unknown"

    def _get_messages(self) -> List[Dict[Any, Any]]:
        if isinstance(self._data, dict):
            return self._get_messages_from_dict()
        return self._get_messages_from_list()

    def _get_messages_from_dict(self) -> List[Dict[Any, Any]]:
        return [self._data.get("message")] # type:ignore

    def _get_messages_from_list(self) -> List[Dict[Any, Any]]:
        messages = []
        for data in self._data:
            message = data.get("message", None)
            if not message:
                continue
            messages.append(message)
        return messages

    def __sniff_schema__(self) -> None:
        messages = self._get_messages()
        if not messages:
            return
        sniffed_schemas = [] # type:ignore
        for message in messages:
            sniffed_schema = {}
            for key, value in message.items():
                sniffed_schema[key] = {
                    "type": self._get_type(value),
                    "tag": "",
                    "description": "",
                    "required": False,
                }
            sniffed_schemas.append({len(sniffed_schemas): sniffed_schema})
        self._sniffed_schema = (
            sniffed_schemas[0][0] if len(sniffed_schemas) == 1 else sniffed_schemas
        )

    @property
    def schema_path(self) -> str:
        return self._schema_path

    @property
    def sniffed_schema_exists(self) -> bool:
        return self._sniffed_schema is not None
