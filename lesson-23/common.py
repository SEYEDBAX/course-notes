from typing import List, Dict, Optional, Union, Any, Generic, TypeVar

def num_plus(num: int = 0) -> int:
    return num + 1

def merge_string(strs: List[str]) -> str:
    return " ".join(strs)

def average_class(members: Dict[str, List[Dict[str, float]]]) -> float:
    """
    this function returns the average of the class members scores

    members: Dict[str, List[Dict[str, float]]]

    sample input:
        average_class({
            "names": [
                {"name": "Alice", "score": 80.0},
                {"name": "Bob", "score": 75.0},
                {"name": "Charlie", "score": 85.0}
            ]
        })
    """
    total: int = len(members["names"])
    sums: float = 0
    for member in members["names"]:
        _, number = member.popitem()
        sums += number
    return sums / total


x: Optional[int] = None
num: Union[int, float] = 0
text: Any = None

T = TypeVar("T")

class Foo(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get_value(self) -> T:
        return self.value
    
    def set_value(self, value: T) -> None:
        self.value = value

foo: Foo[int] = Foo(1)
foo.set_value(2)
foo.get_value()

bar: Foo[str] = Foo("hello")
bar.set_value("world")
bar.get_value()
