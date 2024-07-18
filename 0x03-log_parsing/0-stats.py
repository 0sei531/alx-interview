#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys
import re


def print_stats(total_size, status_codes):
    """Print statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """Parse a line and return file size and status code"""
    pattern = r'^\S+ - \[.+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    match = re.match(pattern, line)
    if match:
        return int(match.group(2)), match.group(1)
    return 0, None


def process_logs():
    """Process logs from stdin"""
    total_size = 0
    status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            size, code = parse_line(line)
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    process_logs()
