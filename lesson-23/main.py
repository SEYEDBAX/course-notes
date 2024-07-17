from common import *

x: int = num_plus(2)


def foo(a: list, b: int) -> int:
    return a + b

bar: int = foo(1, 2)


class Foo: ...


x: Foo = Foo()
