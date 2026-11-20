"""
Emulacja operatorów C# `?.` (null-conditional) i `??` (null-coalescing)
w Pythonie za pomocą klasy opakowującej `Maybe`.

W C#: `user?.Address?.City ?? "brak"` zwraca `"brak"`, gdy którykolwiek
element łańcucha jest `null`, zamiast rzucać wyjątek. Python nie ma takich
operatorów, ale ten sam efekt daje obiekt, który przechwytuje dostęp
do atrybutu (`__getattr__`), indeksowanie (`__getitem__`) i wywołanie
(`__call__`): dopóki w środku jest wartość, deleguje do niej i opakowuje
wynik; gdy w środku jest `None`, zwraca kolejne puste `Maybe`. Na końcu
łańcucha `unwrap(default)` wyciąga wartość albo domyślną.

W Pythonie:

    miasto = Maybe(user).address.city.unwrap('brak')

Kod demonstracyjny jest pod `if __name__ == '__main__'`.
"""
from typing import Any


class Maybe:
    """Opakowanie wartości, która może być `None`; łańcuch operacji nie wybucha."""

    def __init__(self, value: Any) -> None:
        """
        Args:
            value: dowolna wartość albo `None`
        """
        self._value = value

    # __getattr__ jest wywoływane TYLKO wtedy, gdy zwykłe wyszukiwanie atrybutu
    # zawiedzie - dlatego self._value (ustawione w __init__) nie wpada w pętlę
    def __getattr__(self, name: str) -> Maybe:
        """`Maybe(x).atrybut` - dostęp do atrybutu opakowanej wartości."""
        if self._value is None:
            return Maybe(None)
        return Maybe(getattr(self._value, name))

    def __getitem__(self, key: Any) -> Maybe:
        """`Maybe(x)[klucz]` - indeksowanie opakowanej wartości."""
        if self._value is None:
            return Maybe(None)
        return Maybe(self._value[key])

    def __call__(self, *args: Any, **kwargs: Any) -> Maybe:
        """`Maybe(f)(...)` - wywołanie opakowanej wartości."""
        if self._value is None:
            return Maybe(None)
        return Maybe(self._value(*args, **kwargs))

    def unwrap(self, default: Any = None) -> Any:
        """
        Kończy łańcuch: zwraca opakowaną wartość albo `default` (odpowiednik `??`).

        Args:
            default: wartość zwracana, gdy w środku jest `None`
        """
        # wyrażenie warunkowe (ternary): A if warunek else B
        return default if self._value is None else self._value


# C#: user?.Address?.City ?? "brak"
# miasto = Maybe(user).address.city.unwrap("brak")

if __name__ == '__main__':
    from types import SimpleNamespace

    # SimpleNamespace - szybki obiekt z atrybutami, do demonstracji
    user_z_adresem = SimpleNamespace(address=SimpleNamespace(city='Kraków'))
    user_bez_adresu = SimpleNamespace(address=None)

    print(Maybe(user_z_adresem).address.city.unwrap('brak'))   # Kraków
    print(Maybe(user_bez_adresu).address.city.unwrap('brak'))  # brak
    print(Maybe(None).address.city.unwrap('brak'))             # brak

    # bez Maybe ten sam łańcuch na None rzuca AttributeError:
    # user_bez_adresu.address.city
