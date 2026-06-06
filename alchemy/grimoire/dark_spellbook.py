#!/usr/bin/python3
from .dark_validator import dark_validator


def dark_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validate_res = dark_validator(ingredients)
    if "INVALID" in validate_res:
        return f"Spell rejected: {spell_name} ({validate_res})"
    else:
        return f"Spell recorded: {spell_name} ({validate_res})"
