import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    count = random.randint(len(achievements) // 4, len(achievements) * 3 // 4)
    return set(random.sample(achievements, k=count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer']
    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    union = set.union(alice, bob, charlie, dylan)
    print(f"\nAll distinct achievements: {union}")

    intersection = set.intersection(alice, bob, charlie, dylan)
    print(f"\nCommon achievements: {intersection}")

    difference = alice.difference(set.union(bob, charlie, dylan))
    print(f"\nOnly Alice has: {difference}")
    difference = bob.difference(set.union(alice, charlie, dylan))
    print(f"Only Bob has: {difference}")
    difference = charlie.difference(set.union(alice, bob, dylan))
    print(f"Only Charlie has: {difference}")
    difference = dylan.difference(set.union(alice, bob, charlie))
    print(f"Only Dylan has: {difference}")

    print()
    missing = set(achievements).difference(alice)
    print(f"Alice is missing: {missing}")
    missing = set(achievements).difference(bob)
    print(f"Bob is missing: {missing}")
    missing = set(achievements).difference(charlie)
    print(f"Charlie is missing: {missing}")
    missing = set(achievements).difference(dylan)
    print(f"Dylan is missing: {missing}")
