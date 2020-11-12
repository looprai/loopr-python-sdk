import re

"""
Generating slug with name.
"""


def slug_create(name: str):
    a = name.lower().replace(" ", "-")
    return re.sub(r"[^a-zA-Z0-9-_~]", "", a)
