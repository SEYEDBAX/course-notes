## **Working with Lists in Python**

A list is a collection which is ordered and changeable. In Python, lists are written with square brackets.

**Creating a List:**
```python
my_list = [1, 2, 3]
```

**Adding Elements:**
```python
my_list.append(4)  # Adds an element to the end of the list
my_list.insert(1, 'a')  # Inserts an element at a specific position
```

**Removing Elements:**
```python
my_list.remove('a')  # Removes the first occurrence of an element
del my_list[0]  # Removes an element at a specific position
```

**Ten Examples:**
```python
[1, 'apple', 3.14, True, None]
['red', 'green', 'blue']
list(range(10))
[[], [1, 2], [3, 4]]
['a' * i for i in range(1, 11)]
[3] * 10
list('hello')
[0] + [1, 2, 3]
[-1, -2, -3]
['yes' if i % 2 == 0 else 'no' for i in range(10)]
```

## **Working with Tuples in Python**

A tuple is a collection which is ordered and unchangeable. In Python, tuples are written with round brackets.

**Creating a Tuple:**
```python
my_tuple = (1, 2, 3)
```

**Adding Elements:**
Tuples are immutable, so you can't add elements after the tuple has been created. However, you can concatenate tuples.

**Removing Elements:**
Tuples are immutable, so you can't remove elements. You can, however, delete the tuple completely.

**Ten Examples:**
```python
(1, 'apple', 3.14, True, None)
('red', 'green', 'blue')
tuple(range(10))
((), (1, 2), (3, 4))
tuple('hello')
(1,) * 10
(0,) + (1, 2, 3)
(-1, -2, -3)
('yes',) * 5 + ('no',) * 5
(1, 2) * 5
```

## **Working with Sets in Python**

A set is a collection which is unordered, unindexed, and unchangeable, but you can add new items and remove existing ones.

**Creating a Set:**
```python
my_set = {1, 2, 3}
```

**Adding Elements:**
```python
my_set.add(4)  # Adds an element to the set
```

**Removing Elements:**
```python
my_set.remove(2)  # Removes a specific element
my_set.discard(5)  # Removes a specific element without raising an error if the element does not exist
```

**Ten Examples:**
```python
{1, 2, 3, 4, 5}
{'apple', 'banana', 'cherry'}
set('hello')
{True, False, None}
set(range(10))
{3.14, 2.71, 1.41}
{'a', 'b', 'c'} - {'b'}
{'x' * i for i in range(1, 6)}
{(-1)**i for i in range(10)}
{frozenset({i, i + 1}) for i in range(10)}
```

## **Working with Dictionaries in Python**

A dictionary is a collection which is unordered, changeable, and indexed. In Python, dictionaries are written with curly brackets, and they have keys and values.

**Creating a Dictionary:**
```python
my_dict = {'name': 'John', 'age': 30}
```

**Adding Elements:**
```python
my_dict['height'] = 175  # Adds a new key-value pair
```

**Removing Elements:**
```python
del my_dict['age']  # Removes a key-value pair
my_dict.pop('height')  # Removes a key-value pair and returns the value
```

**Ten Examples:**
```python
{'id': 1, 'title': 'Python Basics'}
{'x': 0, 'y': 0, 'z': 0}
{str(i): i**2 for i in range(10)}
{'colors': ['red', 'green', 'blue']}
{'nested': {'a': 1, 'b': 2}}
{True: 'yes', False: 'no'}
{'mixed': [1, 'two', 3.0]}
{'empty': {}}
{'one': 1, 'two': 2, 'three': 3}
{'alpha': set('abc'), 'numeric': set(range(3))}
```