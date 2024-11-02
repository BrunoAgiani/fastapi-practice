from dataclasses import dataclass
from typing import List

@dataclass
class Ponto:
    x: int
    y: int

@dataclass
class ListaDePontos:
    pontos: List[Ponto]


tmp = {'mylist': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}

print(ListaDePontos(**tmp))