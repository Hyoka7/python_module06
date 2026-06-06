#!/usr/bin/python3

from alchemy.potions import healing_potion, strength_potion

if __name__ == "__main__":
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potioon: {healing_potion()}")
