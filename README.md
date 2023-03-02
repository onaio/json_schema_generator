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

## Install Dependencies

```bash
pip install '.[tests]'
```

## Help

```bash
json_schema_generator -h
```

## Run

1. Output to Terminal

   ```bash
   json_schema_generator --source sample_files/sample.json
   ```

2. Pipe to file

   ```bash
   json_schema_generator --source sample_files/sample.json > sample_files/schema.json
   ```

## Test

```bash
pytest
```

Powered by [Genson](https://github.com/wolverdude/GenSON)
