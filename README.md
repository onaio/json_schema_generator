# Generate JSON Schema From JSON File

- Generate a JSON SCHEMA from a passed in `List/Array` of JSON Objects in a JSON file
- Recommended to use a wide sample range of possible objects the schema conforms to

## Create Virtual Env

```bash
python -m venv .venv
```

## Activate Virtual Env

```bash
source .venv/bin/activate
```

## Install

1.  Locally

    ```bash
    git clone git@github.com:onaio/json_schema_generator.git && cd json_schema_generator

    pip install '.[tests]'
    ```

2.  From Github

    ```bash
    pip install json_schema_generator https://github.com/onaio/json_schema_generator/archive/main.zip
    ```

## Help

```bash
json_schema_generator -h
```

## Run

### As a CLI

1. Output to Terminal

   ```bash
   json_schema_generator --source sample_files/sample.json
   ```

2. Pipe to file

   ```bash
   json_schema_generator --source sample_files/sample.json > sample_files/schema.json
   ```

### As a Module

```python
from json_schema_generator import JsonType, generate_schema


def main(record: JsonType):
    return generate_schema(record)


print(main([{"test": "entry"}, [1984]]))

```

## Test

```bash
python -m pytest
```

Powered by [Genson](https://github.com/wolverdude/GenSON)
