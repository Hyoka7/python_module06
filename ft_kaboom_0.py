#!/usr/bin/python3


import alchemy.grimoire

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    spell_name = "Fantasy"
    ingredient = "Earth, wind and fire"
    result = alchemy.grimoire.light_spell_record(spell_name, ingredient)
    print(f"Testing record light_spell: {result}")
