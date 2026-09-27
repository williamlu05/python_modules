import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    players = ['Alice', 'bob', 'Charlie', 'dylan',
               'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    capitalized_only = [
        name for name in players if name.capitalize() == name and name != ""
    ]
    print(f"New list of capitalized names only: {capitalized_only}")

    scores = {name: random.randint(100, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")
    average = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")

    high_scores = {
        name: scores[name] for name in scores if scores[name] > average
    }
    print(f"High scores: {high_scores}")
