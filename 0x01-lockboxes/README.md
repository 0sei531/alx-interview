# Lockboxes Project

## Table of Contents

- [Description](#description)
- [Concepts](#concepts)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Resources](#resources)
- [Author](#author)

## Description

This project involves determining if all boxes can be opened. You have `n` locked boxes, each containing keys to other boxes. The goal is to determine if you can open all the boxes starting from the first one, which is always unlocked.

## Concepts

To solve this problem, you need to understand the following concepts:

- Lists and List Manipulation
- Graph Theory Basics
- Algorithmic Complexity
- Recursion
- Queue and Stack
- Set Operations

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/alx-interview.git
    ```
2. Navigate to the project directory:
    ```bash
    cd alx-interview/0x01-lockboxes
    ```

## Usage

1. Ensure your Python files are executable:
    ```bash
    chmod +x 0-lockboxes.py main_0.py
    ```
2. Run the main script to test the function:
    ```bash
    ./main_0.py
    ```

## Examples

Here's an example of how the function works:

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
