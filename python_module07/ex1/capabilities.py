from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    _transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"

    def attack(self) -> str:
        return "Sproutling uses vine Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def heal(self) -> str:
        return "Bloomelle heals itself and other for a large amount"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def transform(self) -> str:
        self._transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return "Shiftling returns to normal"

    def attack(self) -> str:
        if self._transformed:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def transform(self) -> str:
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return "Morphagon stabilizes its form."

    def attack(self) -> str:
        if self._transformed:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally"


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
