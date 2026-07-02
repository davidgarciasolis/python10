from collections.abc import Callable


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    def nueva_funcion(target: str, power: int) -> tuple[str, str]:
        resultado1 = spell1(target, power)
        resultado2 = spell2(target, power)
        return (resultado1, resultado2)
    return (nueva_funcion)


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int
                    ) -> Callable[[str, int], str]:
    def nueva_funcion(target: str, power: int) -> str:
        poder_amplificado = power * multiplier
        resultado = base_spell(target, poder_amplificado)
        return (resultado)
    return (nueva_funcion)


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    def nueva_funcion(target: str, power: int) -> str:
        if (condition(target, power)):
            return (spell(target, power))
        return ("Spell fizzled")
    return (nueva_funcion)


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    def nueva_funcion(target: str, power: int) -> list[str]:
        resultados = []
        for spell in spells:
            resultados.append(spell(target, power))
        return (resultados)
    return (nueva_funcion)


def fireball(target: str, power: int) -> str:
    return (f"Fireball hits {target} for {power} damage")


def heal(target: str, power: int) -> str:
    return (f"Heals {target} for {power} HP")


def shield(target: str, power: int) -> str:
    return (f"Shield protects {target} with {power} armor")


def enough_power(target: str, power: int) -> bool:
    return (power >= 10)


if __name__ == "__main__":
    target = "Dragon"
    power = 10

    print()
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined(target, power)}")
    print()

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {power}, Amplified: {power * 3}")
    print()

    print("Testing conditional caster...")
    conditional_fireball = conditional_caster(enough_power, fireball)
    print(f"With enough power: {conditional_fireball(target, 15)}")
    print(f"Without enough power: {conditional_fireball(target, 5)}")
    print()

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    print(f"Sequence result: {sequence(target, power)}")
