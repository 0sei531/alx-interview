#!/usr/bin/python3
"""
Task - Script that reads stdin line by line and computes metrics.
"""

import sys


def parse_line(line, st_code):
    """Read, parse and grab data."""
    try:
        parsed_line = line.split()
        status_code = parsed_line[-2]
        if status_code in st_code.keys():
            st_code[status_code] += 1
        return int(parsed_line[-1])
    except (IndexError, ValueError):
        return 0

def print_stats(file_size, st_code):
    """Print stats in ascending order."""
    print("File size: {}".format(file_size))
    for key in sorted(st_code.keys()):
        if st_code[key]:
            print("{}: {}".format(key, st_code[key]))

def main():
    """Main function to read stdin and compute metrics."""
    st_code = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    file_size = 0
    count = 1

    try:
        for line in sys.stdin:
            file_size += parse_line(line, st_code)
            if count % 10 == 0:
                print_stats(file_size, st_code)
            count += 1
    except KeyboardInterrupt:
        print_stats(file_size, st_code)
        raise
    print_stats(file_size, st_code)

if __name__ == "__main__":
    main()
