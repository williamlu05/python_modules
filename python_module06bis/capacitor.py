from ex3 import TransformCapability, TransformCreatureFactory


if __name__ == "__main__":
    print("Testing Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    print(" base:")
    base_transform = transform_factory.create_base()
    print(base_transform.describe())
    print(base_transform.attack())
    if isinstance(base_transform, TransformCapability):
        print(base_transform.transform())
        print(base_transform.attack())
        print(base_transform.revert())

    print(" evolved:")
    evolved_transform = transform_factory.create_evolved()
    print(evolved_transform.describe())
    print(evolved_transform.attack())
    if isinstance(evolved_transform, TransformCapability):
        print(evolved_transform.transform())
        print(evolved_transform.attack())
        print(evolved_transform.revert())
