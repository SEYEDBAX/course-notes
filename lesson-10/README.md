# Object-Oriented Programming in Python

## Understanding Object Orientation
Object-oriented programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. It utilizes several techniques from previously established paradigms, including modularity, polymorphism, and encapsulation.

### Key Concepts of OOP:
- **Classes & Objects**: Classes are blueprints for creating objects (a particular data structure), providing initial values for state (member variables) and implementations of behavior (member functions or methods).
- **Inheritance**: Objects can inherit characteristics from other classes.
- **Polymorphism**: Objects can share the same interface for different underlying forms (data types).
- **Encapsulation**: Each object keeps its state private, inside a class.

## Object Orientation in Python
Python is a multi-paradigm language that supports object-oriented programming. In Python, everything is an object, and classes are used to create new objects.

### Creating a Class in Python:
```python
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def greet(self):
        return f"Hello, I am a {self.name} and I can go up to {self.max_speed} km/h!"
```

### Magic Methods in Python:
Magic methods in Python are special methods that start and end with double underscores (`__`). They are also known as dunder methods. These methods enable us to emulate the behavior of built-in types.

#### Common Magic Methods:
- `__init__`: For initializing new objects.
- `__str__`: For creating a human-readable representation of an object.
- `__repr__`: For creating an unambiguous representation of an object.
- `__add__`: For defining behavior for the addition operator `+`.

#### Using Magic Methods:
```python
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def __str__(self):
        return f"{self.name} ({self.max_speed} km/h)"

    def __repr__(self):
        return f"Vehicle('{self.name}', {self.max_speed})"

    def __add__(self, other):
        return Vehicle(f"{self.name} & {other.name}", self.max_speed + other.max_speed)

# Example Usage:
car = Vehicle("Car", 150)
bike = Vehicle("Bike", 80)
print(car)  # Output: Car (150 km/h)
print(car + bike)  # Output: Car & Bike (230 km/h)
```

This pamphlet provides a brief overview of object-oriented programming in Python, including the creation of classes and the use of magic methods. By understanding these concepts, you can write more organized and efficient code that leverages the power of OOP in Python.

Certainly! Let's delve a bit deeper into Object-Oriented Programming (OOP) in Python with a more comprehensive example. We'll create a `Book` class to illustrate various OOP concepts such as inheritance, encapsulation, and polymorphism.

```python
# Base class
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def get_genre(self):
        return self.genre

# Inherited class
class Novel(Book):
    def __init__(self, title, author, genre, protagonist):
        super().__init__(title, author, genre)
        self.protagonist = protagonist

    def get_protagonist(self):
        return self.protagonist

# Another inherited class
class AcademicBook(Book):
    def __init__(self, title, author, genre, field):
        super().__init__(title, author, genre)
        self.field = field

    def get_field(self):
        return self.field

# Using the classes
my_novel = Novel("1984", "George Orwell", "Dystopian", "Winston Smith")
my_textbook = AcademicBook("A Brief History of Time", "Stephen Hawking", "Science", "Physics")

print(my_novel)  # Output: '1984' by George Orwell
print(f"Genre: {my_novel.get_genre()}")  # Output: Genre: Dystopian
print(f"Protagonist: {my_novel.get_protagonist()}")  # Output: Protagonist: Winston Smith

print(my_textbook)  # Output: 'A Brief History of Time' by Stephen Hawking
print(f"Field: {my_textbook.get_field()}")  # Output: Field: Physics
```

In this example:
- The `Book` class is our base class with common attributes like `title`, `author`, and `genre`.
- The `Novel` class inherits from `Book` and adds a specific attribute `protagonist`.
- The `AcademicBook` class also inherits from `Book` but has a different attribute `field` for the academic field of study.
- We use the `super()` function to call the `__init__` method of the parent class, allowing us to avoid repeating code.
- The `__str__` method provides a string representation of our objects, making them more readable.
- We demonstrate encapsulation by using methods like `get_genre()`, `get_protagonist()`, and `get_field()` to access object attributes.

This example showcases the power and flexibility of OOP in Python, enabling you to create complex data structures that are easy to manage and extend.