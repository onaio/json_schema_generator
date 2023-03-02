import argparse
import json
import sys

from .generate import generate_schema

"""
CLI to generate a JSON Schema 
From a file with a list of JSON Objects.

Ideally pass in more than one object
For a nice sample range.
"""


parser = argparse.ArgumentParser(
    description="Generate a JSON schema from a list of JSON objects"
)
parser.add_argument(
    "--source",
    help="Source File with JSON List",
    metavar="sample.json",
    type=argparse.FileType(mode="r"),
    required=True,
)
args = parser.parse_args()

try:
    file_data = json.load(args.source)
except json.JSONDecodeError:
    sys.exit("Error: Source file could not be read. Pass in a valid JSON file")

if type(file_data) is not list:
    sys.exit(
        "Error: Source file validation failed. Pass in a valid list of JSON objects"
    )


def run():
    try:
        generate_json_schema = generate_schema(file_data)
        print(generate_json_schema)
    except Exception as err:
        sys.exit(f"Error: Schema generation failed: {err}")


def main():
    run()


if __name__ == "__main__":
    run()
