# Island Perimeter

## Project Overview

This project is a Python-based algorithm that calculates the perimeter of an island in a grid (2D list). The grid is represented by `1`s (land) and `0`s (water), and the task is to determine the perimeter of the island (group of connected `1`s). The island is surrounded by water and there is no water inside the island.

The problem is solved using efficient iteration and logical operations to ensure optimal performance, adhering to the project's constraints.

## Requirements

- **Python Version:** Python 3.4.3 (will be interpreted/compiled on Ubuntu 20.04 LTS)
- **Allowed Editors:** vi, vim, emacs
- **Coding Style:** The code must adhere to PEP 8 (version 1.7)
- **Modules:** No additional modules or libraries are allowed to be imported
- **Documentation:** All modules and functions must be documented
- **File:** `0-island_perimeter.py` should be executable (`chmod +x`)
  
## Usage

### Running the Script

To run the island perimeter calculation, follow the steps below:

1. Ensure that Python 3.4.3 is installed on your system.
2. Make the Python file executable using the following command:

    ```bash
    chmod +x 0-island_perimeter.py
    ```

3. Run the script in the terminal by importing it in a Python program:

    ```bash
    ./0-main.py
    ```

### Example Input and Output

Given the following grid:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
