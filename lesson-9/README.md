## Python Handout: Common Concepts and Examples

### 1. **Try-Except (Error Handling)**
- **Purpose**: To handle exceptions (errors) gracefully.
- **Syntax**:
    ```python
    try:
        # Code that might raise an exception
    except ExceptionType as e:
        # Code to handle the exception
    ```

- **Example**:
    ```python
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    ```

### 2. **Splitting Strings**
- **Purpose**: To split a string into a list of substrings based on a delimiter.
- **Syntax**:
    ```python
    string = "Hello, World!"
    parts = string.split(",")  # Split by comma
    ```

- **Example**:
    ```python
    sentence = "Python is awesome"
    words = sentence.split()  # Split by space (default)
    print(words)  # Output: ['Python', 'is', 'awesome']
    ```

### 3. **Regular Expressions (Regex)**
- **Purpose**: To search, match, and manipulate text patterns.
- **Syntax**:
    ```python
    import re
    pattern = r"\d{3}-\d{2}-\d{4}"  # Example: Social Security Number pattern
    result = re.match(pattern, input_string)
    ```

- **Example**:
    ```python
    import re
    text = "My SSN is 123-45-6789"
    ssn_pattern = r"\d{3}-\d{2}-\d{4}"
    match = re.search(ssn_pattern, text)
    if match:
        print("Found SSN:", match.group())
    else:
        print("No SSN found.")
    ```

### 4. **Working with Dates and Times**
- **Datetime Module**:
    ```python
    from datetime import datetime, timedelta

    now = datetime.now()
    print("Current date and time:", now)

    tomorrow = now + timedelta(days=1)
    print("Tomorrow:", tomorrow.strftime("%Y-%m-%d %H:%M:%S"))
    ```

- **Time Module**:
    ```python
    import time

    timestamp = time.time()
    print("Current timestamp:", timestamp)

    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    print("Formatted time:", formatted_time)
    ```