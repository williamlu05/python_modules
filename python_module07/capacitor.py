import ex0
from ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    print("Base:")
    base_heal = healing_factory.create_base()
    print(base_heal.describe())
    print(base_heal.attack())
    print(base_heal.heal())
    print("Evolved:")
    evolved_heal = healing_factory.create_evolved()
    print(evolved_heal.describe())
    print(evolved_heal.attack())
    print(evolved_heal.heal())

    transform_factory = TransformCreatureFactory()
    print("\nBase:")
    base_transform = transform_factory.create_base()
    print(base_transform.describe())
    print(base_transform.attack())
    print(base_transform.transform())
    print("Evolved:")
    evolved_transform = transform_factory.create_evolved()
    print(evolved_transform.describe())
    print(evolved_transform.attack())
    print(evolved_transform.transform())