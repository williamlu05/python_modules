import random
from typing import Generator


def gen_event(
    players: tuple[str, ...], actions: tuple[str, ...]
) -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        yield events.pop(random.randint(0, len(events) - 1))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    players = ("alice", "bob", "charlie", "dylan")
    actions = ("run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release", "use")

    stream = gen_event(players, actions)
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    events: list[tuple[str, str]] = []
    for _ in range(10):
        events.append(next(stream))
    print(f"Built list of {len(events)} events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
