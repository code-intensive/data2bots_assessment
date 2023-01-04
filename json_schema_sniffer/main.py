from json_schema_sniffer.sniffers.schema_sniffer import SchemaSniffer
from json_schema_sniffer.storages.json_file_storage import LocalJsonFileStorage
from json_schema_sniffer.validators.json_validator import JsonValidator


def main() -> None:
    json_path = "data/data_1.json"
    schema_sniffer = SchemaSniffer(
        json_path=json_path,
        validator=JsonValidator,  # type: ignore
        storage=LocalJsonFileStorage,  # type: ignore
    )
    schema_sniffer.sniff_schema()
    schema_sniffer.save(file_name="./schema3", base_path="./schema")  # type: ignore


if __name__ == "__main__":
    main()
