def recursive_harvest(number, harvest_days) -> None:
    if number > harvest_days:
        print("Harvest time!")
    else:
        print("Day", number)
        recursive_harvest(number + 1, harvest_days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive_harvest(1, days)
