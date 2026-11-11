from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory

from ex4 import (AggressiveStrategy, BattleStrategy, InvalidStrategyException,
                 NormalStrategy)


def battle(
    opponents: list[tuple[CreatureFactory, type[BattleStrategy]]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory1, strategy1 = opponents[i]
                factory2, strategy2 = opponents[j]
                fighter1 = factory1.create_base()
                fighter2 = factory2.create_base()

                print(fighter1.describe())
                print(" vs.")
                print(fighter2.describe())
                print("fight!")
                strategy1(fighter1).act()
                strategy2(fighter2).act()
    except InvalidStrategyException as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle([(flame_factory, NormalStrategy),
            (transform_factory, AggressiveStrategy)])

    print("\nTournament 1 (error)")
    print(" [ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    battle([(transform_factory, AggressiveStrategy),
            (flame_factory, AggressiveStrategy)])

    print("\nTournament 2")
    print(" [ (Flameling+Normal), (Shiftling+Aggressive),"
          " (Shiftling+Normal) ]")
    battle([(flame_factory, NormalStrategy),
            (transform_factory, AggressiveStrategy),
            (transform_factory, NormalStrategy)])
