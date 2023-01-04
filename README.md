# JSON Schema Sniffer

## HOW TO:
### Installing requirements:
##### Using pip:

```bash
pip install -r requirements.txt

```

##### Using Poetry:
```bash
# if you do not have poetry on your system you could simply install it via pip using "pip install poetry".

poetry shell && poetry install

```

### Running test using pytest:

```bash
# Running tests using pytest, use the command below.

pytest .

```

### Type checking using MYPY:

```bash
# To run typecheck, issue the command below.

mypy .

```

### Order import statements using isort:

```bash
isort .
```

### To run the program:
##### From the root project directory:
```bash
python -m json_schema_sniffer

# if python2 exists in your PATH you may want to issue the command using

python3 -m json_schema_sniffer

```
