from abc import ABC, abstractmethod

from ex3.creature import Creature, TransformCapability


class InvalidStrategyException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class BattleStrategy(ABC):
    def __init__(self, creature: Creature) -> None:
        self._creature = creature

    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self, creature: Creature) -> None:
        super().__init__(creature)

    def act(self) -> None:
        print(self._creature.attack())

    def is_valid(self) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def __init__(self, creature: Creature) -> None:
        super().__init__(creature)

    def act(self) -> None:
        if not self.is_valid():
            raise InvalidStrategyException(
                f"Invalid Creature '{self._creature.name()}' "
                "for this aggressive strategy"
            )
        if isinstance(self._creature, TransformCapability):
            print(self._creature.transform())
            print(self._creature.attack())
            print(self._creature.revert())

    def is_valid(self) -> bool:
        return isinstance(self._creature, TransformCapability)
