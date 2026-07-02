from functools import wraps
from collections.abc import Callable
import time
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"Spell completed in {elapsed_time:.3f} seconds")

        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[-1]
            if power >= min_power:
                return (func(*args, **kwargs))
            return ("Insufficient power for this spell")
        return (wrapper)
    return (decorator)


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return (func(*args, **kwargs))
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt "
                              f"{attempt}/{max_attempts})")
                    else:
                        return (f"Spell casting failed after "
                                f"{max_attempts} attempts")
        return (wrapper)
    return (decorator)


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3
                and all(c.isalpha() or c.isspace() for c in name))

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


@retry_spell(3)
def failing_spell() -> str:
    raise Exception("Spell fizzled")


@retry_spell(3)
def waaagh_spell() -> str:
    return ("Waaaaaaagh spelled !")


def main() -> None:
    print("Testing spell timer...")
    print(f"Result: {fireball()}")
    print()

    print("Testing retrying spell...")
    print(failing_spell())
    print(waaagh_spell())
    print()

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
    print()


if __name__ == "__main__":
    main()
