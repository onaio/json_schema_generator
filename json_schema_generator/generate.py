from typing import Iterable, Mapping, Sequence, Union

from genson import SchemaBuilder

JsonType = Union[
    Mapping[str, "JsonType"], Sequence["JsonType"], str, int, float, bool, None
]


def generate_schema(records: Iterable[JsonType]) -> str:
    """Generate a JSON Schema from a `List` of JSON Objects.

    This function samples objects from a list of JSON objects
    and generates a unified schema conforming to all of them.

    Parameters
    ----------
    records : Iterable[JsonType]
        A `List` of objects or scalars that can be serialized in JSON (default is None)

    Returns
    -------
    JSON string
        A JSON Schema

    Example
    --------
    >>> generate_schema([{}, [], 1984])
    {"$schema": "http://json-schema.org/schema#", "type": ["array", "integer", "object"]}
    """

    builder = SchemaBuilder()
    for record in records:
        builder.add_object(record)
    # empty object to ensure schema is not too restrictive
    # i.e no field is required
    builder.add_object({})
    schema = builder.to_json()
    return schema
