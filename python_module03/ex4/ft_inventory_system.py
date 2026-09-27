import sys


def add_entry(result: dict[str, int], string: str) -> None:
    entry = string.split(":")
    if len(entry) != 2 or entry[0] == "":
        print(f"Error - invalid parameter '{string}'")
        return
    key = entry[0]
    if key in result:
        print(f"Redundant item '{key}' - discarding")
        return
    try:
        value = int(entry[1])
        if value < 0:
            print(f"Error - invalid parameter '{string}'")
            return
        result.update({key: value})
    except ValueError as e:
        print(f"Quantity error for '{key}': {e}")


def manage_entries() -> dict[str, int]:
    result: dict[str, int] = {}
    count = 1
    while count < len(sys.argv):
        string = sys.argv[count]
        add_entry(result, string)
        count += 1
    return result


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = manage_entries()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory.keys())} items: {total}")

    for item in inventory.keys():
        percentage = 0.0 if total == 0 else inventory[item] * 100 / total
        print(f"Item {item} represents {round(percentage, 1)}%")

    if len(inventory) > 0:
        most = list(inventory.keys())[0]
        least = most
        for item in inventory.keys():
            if inventory[item] > inventory[most]:
                most = item
            if inventory[item] < inventory[least]:
                least = item
        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(f"Item least abundant: {least} with quantity {inventory[least]}")
    add_entry(inventory, "magic_item:1")
    print(f"Updated inventory: {inventory}")
