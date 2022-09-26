from statistics import mean
from typing import List, Set, Dict, Tuple

def print_indices_and_elements(elements) -> None:
    for idx, elem in enumerate(elements):
        print(idx, elem)


def get_even_numbers_between(start: int, end: int) -> List[int]:
    return [i for i in range(start, end+1) if not i%2]


def get_char_set_from(s: str) -> Set[str]:
    return {c for c in s}


def get_perfect_squares_between(start: int, end: int) -> Dict[int,int]:
    return {i:i**0.5 for i in range(start+1, end+1) if i**0.5 == int(i**0.5) }


def filter_even_from(numbers: List[int]) -> List[int]:
    return [even for even in numbers if not even%2]


def get_number_or_minus_one(n: int) -> int:
    return n if not n%2 else -1


def transform_multiples_of_5(numbers: List[int]) -> List[int]:
    return [c if not c%2 else -1 for c in numbers if not c%5]


def str_lengths(strings: List[str]) -> List[int]:
    return [len(s) for s in strings]


def get_fibonacci_type(version: int) -> str:
    return "<class 'generator'>" if version == 1 else "<class 'list'>" if version == 2 else ''


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return '123456789012345678901234567890'


class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        self.i = 0
        self.n = len(elements)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 2
            return self.elements[i]
        else:
            raise StopIteration()


def my_avg(e1: float, e2: float, *others: Tuple[float]) -> float:
    return mean((e1,e2) + others)


def keys_with_different_value() -> List[int]:
    return sorted([])

def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        # You should add code here and remove the break
        break

    if numbers:
        # You should add code here
        pass


def append_range(start: int, end: int, step: int=1, to: List[int]=[]):
    # You may add code here

    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value == None
