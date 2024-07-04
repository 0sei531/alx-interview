#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

More info:
- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    Args:
        boxes (list of lists): A list where each element is a list
                               of keys contained in the corresponding box.
    
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    
    Variables:
        myKeys (list): List to store the keys collected.
        key (int): Current key being used to open boxes.
        boxKey (int): Key found inside a specific box.
    """
    myKeys = [0]
    for key in myKeys:
        for boxKey in boxes[key]:
            if boxKey not in myKeys and boxKey < len(boxes):
                myKeys.append(boxKey)
    return len(myKeys) == len(boxes)
