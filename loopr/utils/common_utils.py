import re
from datetime import datetime

"""
Generating slug with name.
"""


def slug_create(name: str):
    a = name.lower().replace(" ", "-")
    return re.sub(r"[^a-zA-Z0-9-_~]", "", a)


def encode_dict(field_values: dict):
    for key, value in field_values.items():
        if isinstance(value, datetime):
            field_values[key] = str(value)
    return field_values
