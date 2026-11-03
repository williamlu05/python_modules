from .. import potions
from .. import elements as e1
import elements as e2


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: "
        f"brew '{e1.create_air()}' and '{potions.strength_potion()}' "
        f"mixed with '{e2.create_fire()}'"
    )
