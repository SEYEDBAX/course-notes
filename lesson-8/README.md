### Modules
A **module** in Python is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` added. When you create a Python file, you're essentially creating a module. You can use any Python file as a module by executing an `import` statement in some other Python file.

**Creating a Module:**
To create a module, simply save the code you want in a file with the file extension `.py`. For example:

```python
# mymodule.py
def greeting(name):
    print(f"Hello, {name}")
```

**Using a Module:**
You can use the module by importing it into another script:

```python
# import the module
import mymodule

# use the module's function
mymodule.greeting("Alice")
```

### Libraries
A **library** is a collection of modules. It's not a single file but a set of modules that provide a related set of functionalities. Python's standard library is a large collection of modules that provides standardized solutions for many problems in programming.

### Frameworks
A **framework**, on the other hand, is a step further than a library. It's a collection of libraries and modules that provides a foundation on which you can build programs for a specific domain. A framework dictates the structure and flow of your program.

**Creating a Custom Module:**
1. Define functions and classes you want to include.
2. Save them in a `.py` file.
3. Import and use them in other Python scripts.

**Examples:**
1. A simple module for arithmetic operations:
```python
# arithmetic.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
```

2. A module for handling geometrical shapes:
```python
# shapes.py
import math

def circle_area(radius):
    return math.pi * radius ** 2

def square_area(side):
    return side * side
```

### Exercises
1. **Create a module**: Write a module named `utilities.py` that contains a function to calculate the factorial of a number and another to check if a number is prime.
2. **Use a module**: Import the `utilities.py` module and use its functions to calculate the factorial of 5 and check if 7 is a prime number.
3. **Extend a module**: Add a function to `utilities.py` that calculates the nth Fibonacci number, then use this function in another script.
