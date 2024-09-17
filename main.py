from typing import Union


def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


if __name__ == "__main__":
    print(add(1, 2))
    print(add(3, 2.5))
    print(add(1.1, 223))
    print(add(100, 22))
