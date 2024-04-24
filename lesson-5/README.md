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

## **Python Functions: A Beginner's Guide**

### **1. Creating Functions**

A function in Python is a reusable block of code that performs a specific task. Here's how you can create your own functions:

```python
def greet(name):
    """Prints a friendly greeting."""
    print(f"Hello, {name}!")

# Call the function
greet("Alice")
```

- The `def` keyword is used to define a function.
- `greet` is the function name.
- `(name)` is the parameter (input) the function accepts.
- The triple-quoted string is a docstring that describes what the function does.

### **2. Function Parameters and Arguments**

- Parameters are placeholders in the function definition.
- Arguments are the actual values passed to the function when calling it.

### **3. Returning Values**

You can use the `return` statement to send a value back from a function:

```python
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(3, 5)
print(f"Result: {result}")
```

### **4. Default Arguments**

You can set default values for function parameters:

```python
def greet(name="Guest"):
    """Greets the user."""
    print(f"Hello, {name}!")

greet()  # Uses the default value
greet("Bob")  # Overrides the default value
```

### **5. Higher-Order Functions**

Python allows functions to be passed as arguments to other functions. These are called higher-order functions:

```python
def apply(func, x, y):
    """Applies a function to two arguments."""
    return func(x, y)

result = apply(add, 10, 20)
print(f"Result: {result}")
```

### **6. Recursive Functions**

A function can call itself. This is useful for solving problems that can be broken down into smaller subproblems:

```python
def factorial(n):
    """Calculates the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 5! = 120
```

