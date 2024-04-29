# Python File Handling Guide

## For Beginners

**Getting Started with Files**
- **What is a File?** A file is a collection of data stored on a disk, identified by a filename.
- **Basic Operations:** Opening, reading, writing, closing, renaming, and deleting files.

**Opening a File**
```python
# Open a file in read mode
file = open('example.txt', 'r')
```

**Reading from a File**
```python
# Read the entire file
content = file.read()
print(content)
```

**Writing to a File**
```python
# Open a file in write mode
file = open('example.txt', 'w')
file.write('Hello, Python!')
```

**Closing a File**
```python
# Always close the file when you're done
file.close()
```

## For Experts

**Advanced File Operations**
- **File Seeking:** Use `file.seek(offset)` to change the file's current position.
- **Context Managers:** Use `with` statement for better management of file operations.

**Working with Binary Files**
```python
# Reading from a binary file
with open('image.png', 'rb') as file:
    binary_data = file.read()
```

**Error Handling**
```python
# Using try-except to handle potential errors
try:
    with open('example.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('File does not exist.')
```

**File Paths**
- **Absolute Path:** Specifies the exact location on the filesystem.
- **Relative Path:** Specifies the path relative to the current working directory.

**File Permissions**
- **Reading ('r'):** Allows you to read the file.
- **Writing ('w'):** Allows you to write to the file.
- **Appending ('a'):** Allows you to add content to the end of the file.



Summarize the I/O behaviors:

|          Mode          |  r   |  r+  |  w   |  w+  |  a   |  a+  |
| :--------------------: | :--: | :--: | :--: | :--: | :--: | :--: |
|          Read          |  +   |  +   |      |  +   |      |  +   |
|         Write          |      |  +   |  +   |  +   |  +   |  +   |
|         Create         |      |      |  +   |  +   |  +   |  +   |
|         Cover          |      |      |  +   |  +   |      |      |
| Point in the beginning |  +   |  +   |  +   |  +   |      |      |
|    Point in the end    |      |      |      |      |  +   |  +   |

Decision tree for the table above:


[![][1]][1]


  [1]: https://i.stack.imgur.com/xVhm8.png