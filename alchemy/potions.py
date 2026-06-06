import alchemy.elements
from elements import create_fire, create_water


def healing_potion() -> str:
    earth = alchemy.elements.create_earth()
    air = alchemy.elements.create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    fire = create_fire()
    water = create_water()
    return f"Strength potion brewed with '{fire}'and '{water}'"
