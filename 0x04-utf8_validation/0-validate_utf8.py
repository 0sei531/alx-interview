#!/usr/bin/python3
"""Determines if a given dataset represents a valid UTF-8 encoding"""


def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.

    Args:
    data (List[int]): A list of integers representing byte data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    bit1 = 1 << 7
    bit2 = 1 << 6
    nbytes = 0

    for num in data:
        # Check the binary representation of the byte
        if nbytes == 0:
            # Count the number of leading 1's
            while (num & bit1):
                nbytes += 1
                bit1 >>= 1

            # If no leading 1's, it's a 1-byte character
            if nbytes == 0:
                continue

            # If it's an invalid UTF-8 byte count
            (1-byte with leading 1 or more than 4 bytes)
            if nbytes == 1 or nbytes > 4:
                return False

            # Reset the bit1 for the next byte
            bit1 = 1 << 7

        else:
            # Check if it's a valid continuation byte (starts with 10)
            if not (num & bit1 and not (num & bit2)):
                return False

        nbytes -= 1

    # Ensure no pending bytes to process
    return nbytes == 0
