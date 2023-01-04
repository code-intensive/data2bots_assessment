from json_validator import JsonValidator
from schema_sniffer import SchemaSniffer
from storages import LocalJsonFileStorage


def main() -> None:
    json_path = "../data/data_1.json"
    schema_sniffer = SchemaSniffer(
        json_path=json_path,
        validator=JsonValidator,
        storage=LocalJsonFileStorage,
    )
    schema_sniffer.sniff_schema()
    schema_sniffer.save("./schema3", base_path="../schema")


if __name__ == "__main__":
    main()
