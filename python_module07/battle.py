from ex0 import AquaFactory, CreatureFactory, FlameFactory


def create_pokemon(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolution = factory.create_evolved()
    print(evolution.describe())
    print(evolution.attack())


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    base = factory1.create_base()
    print(base.describe())
    print("vs.")
    base2 = factory2.create_base()
    print(base2.describe())

    print("fight!")
    print(base.attack())
    print(base2.attack())


if __name__ == "__main__":
    flame_pokemon = FlameFactory()
    create_pokemon(flame_pokemon)
    print()
    water_pokemon = AquaFactory()
    create_pokemon(water_pokemon)
    print()
    fight(flame_pokemon, water_pokemon)
