# 0x04. UTF-8 Validation

## Project Overview

This project involves implementing a Python function to validate whether a given dataset represents a valid UTF-8 encoding. UTF-8 is a variable-length encoding scheme that can use 1 to 4 bytes for each character. The challenge is to ensure that a list of integers correctly represents valid UTF-8 encoded data.

## Requirements

- Python 3.4.3 or higher
- Ubuntu 20.04 LTS
- Adherence to PEP 8 style guide (version 1.7.x)
- Code should be executable and end with a new line

## File Structure

- `0-validate_utf8.py`: Contains the implementation of the `validUTF8` function.
- `0-main.py`: A test file to validate the functionality of the `validUTF8` function.
- `README.md`: This file providing an overview of the project.

## Function Prototype

```python
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    data (List[int]): A list of integers representing byte data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
