from . import elements as e1
from .elements import create_earth
import elements as e2


def healing_potion() -> str:
    return (
        "Healing potion brewed with "
        f"'{create_earth()}' and '{e1.create_air()}'"
    )


def strength_potion() -> str:
    return (
        "Strength potion brewed with "
        f"'{e2.create_fire()}' and '{e2.create_water()}'"
    )
