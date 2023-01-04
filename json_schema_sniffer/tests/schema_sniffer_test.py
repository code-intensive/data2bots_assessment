# type: ignore

from json_schema_sniffer.sniffers.schema_sniffer import SchemaSniffer
from json_schema_sniffer.storages.json_file_storage import LocalJsonFileStorage
from json_schema_sniffer.validators.json_validator import JsonValidator


def test_sniff_schema_types(test_schema_path: str) -> None:
    schema_sniffer = SchemaSniffer(
        json_path=test_schema_path,
        validator=JsonValidator,
        storage=LocalJsonFileStorage,
    )
    schema_sniffer.sniff_schema()
    sniffed_schema = schema_sniffer.retrieve_schema()

    assert sniffed_schema["user"]["type"] == "array"
    assert sniffed_schema["time"]["type"] == "int"
    assert sniffed_schema["internationalCountries"]["type"] == "enum"


def test_sniff_schema_defaults(test_schema_path: str) -> None:
    schema_sniffer = SchemaSniffer(
        json_path=test_schema_path,
        validator=JsonValidator,
        storage=LocalJsonFileStorage,
    )
    schema_sniffer.sniff_schema()
    sniffed_schema = schema_sniffer.retrieve_schema()

    assert sniffed_schema["user"]["required"] is False
    assert sniffed_schema["time"]["required"] is False
    assert sniffed_schema["internationalCountries"]["required"] is False

    assert sniffed_schema["user"]["tag"] == ""
    assert sniffed_schema["time"]["tag"] == ""
    assert sniffed_schema["internationalCountries"]["tag"] == ""

    assert sniffed_schema["user"]["description"] == ""
    assert sniffed_schema["time"]["description"] == ""
    assert sniffed_schema["internationalCountries"]["description"] == ""
