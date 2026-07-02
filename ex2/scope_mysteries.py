from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[..., int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return (count)
    return (counter)


def spell_accumulator(initial_power: int) -> Callable[..., int]:
    total_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power
        return (total_power)
    return (accumulator)


def enchantment_factory(enchantment_type: str) -> Callable[..., str]:
    def enchant(item_name: str) -> str:
        return (f"{enchantment_type} {item_name}")
    return (enchant)


def memory_vault() -> dict[str, Callable[..., Any]]:
    memories = {}

    def store(key: str, value: str) -> None:
        memories[key] = value

    def recall(key: str) -> Any:
        return memories.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall,
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")
    print()

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'name': {vault['recall']('name')}")
    print()

    print("Extra tests...")

    second_accumulator = spell_accumulator(10)
    print(f"Base 10, add 5: {second_accumulator(5)}")
    print(f"First accumulator add 10: {accumulator(10)}")

    print()
    vault["store"]("name", "Sage Closure")
    print(f"Store 'name' = {vault['store']('name', 'Sage Closure')}")
    print(f"Recall 'name': {vault['recall']('name')}")
