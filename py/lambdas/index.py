from functools import reduce
from typing import List, Callable, TypeVar

dollars = ["$ 32.00", "$ 15.00", "$ 12.00", "$ 17.00", "$ 20.00"]

prices = map(lambda dollar: int(float(dollar[1:7])), dollars)
expensive = filter(lambda price: price >= 20, prices)
total = reduce(lambda acum, price: acum+price, expensive, 0)
# print(total)


E = TypeVar("E")
R = TypeVar("R")
A = TypeVar("A")


def map(iterable: List[E], fun: Callable[[E], R]) -> List[R]:
    mapped: List[R] = []

    for e in iterable:
        mapped.append(fun(e))

    return mapped


def filter(iterable: List[E], fun: Callable[[E], bool]) -> List[E]:
    filtered: List[E] = []
    for e in iterable:
        if fun(e):
            filtered.append(e)

    return filtered


def reduce(iterable: List[E], fun: Callable[[A, E], A], acum: A) -> A:
    for e in iterable:
        acum = fun(acum, e)

    return acum


prices = map(dollars, lambda dollar: int(float(dollar[1:7])))
expensive = filter(prices, lambda price: price >= 20)
total = reduce(expensive, lambda acum, price: acum+price, 0)
print(total)
