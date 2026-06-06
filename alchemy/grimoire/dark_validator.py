#!/usr/bin/python3
from .dark_spellbook import dark_allowed_ingredients


def dark_validator(ingredients: str) -> str:
    for ingredient in dark_allowed_ingredients():
        if ingredient in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
