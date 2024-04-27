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

