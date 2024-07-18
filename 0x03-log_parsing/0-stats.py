#!/usr/bin/python3
import sys
import signal
import re

total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

# Regular expression to match the log line format
log_regex = re.compile(r'^.* - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_stats():
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")

def signal_handler(sig, frame):
    """Handles the SIGINT signal."""
    print_stats()
    sys.exit(0)

# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line = line.strip()
    match = log_regex.match(line)
    if match:
        status_code = match.group(1)
        file_size = int(match.group(2))

        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

# Print final stats if there are remaining lines
print_stats()
