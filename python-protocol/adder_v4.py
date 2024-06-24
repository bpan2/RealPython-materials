from typing import Protocol, TypeVar

T = TypeVar("T", bound=int | float | str)


class Adder(Protocol[T]):
    def add(self, x: T, y: T) -> T:
        ...


class IntAdder:
    def add(self, x: int, y: int) -> int:
        return x + y


class FloatAdder:
    def add(self, x: float, y: float) -> float:
        return x + y


class StrAdder:
    def add(self, x: str, y: str) -> str:
        return x + y


def add(adder: Adder) -> None:
    print(adder.add(2, 3))


add(IntAdder())
add(FloatAdder())
add(StrAdder())