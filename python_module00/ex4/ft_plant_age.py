def ft_plant_age() -> None:
    harvest = int(input("Enter plant age in days: "))
    if harvest > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
