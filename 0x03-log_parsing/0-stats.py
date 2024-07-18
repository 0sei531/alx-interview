#!/usr/bin/python3
"""
Log parsing script that reads from standard input and computes metrics.
"""

import sys
import re


def extract_input(input_line):
    """
    Extracts sections of a line of an HTTP request log.
    """
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_stats(stats, total_file_size):
    """
    Prints the accumulated metrics.
    """
    print("File size: {}".format(total_file_size))
    for key in sorted(stats.keys()):
        if stats[key] > 0:
            print("{}: {}".format(key, stats[key]))


def update_metrics(line, total_file_size, stats):
    """
    Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    """
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in stats:
        stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    """
    Starts the log parser.
    """
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    try:
        for line in sys.stdin:
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats
            )
            line_num += 1
            if line_num % 10 == 0:
                print_stats(status_codes_stats, total_file_size)
    except (KeyboardInterrupt, EOFError):
        print_stats(status_codes_stats, total_file_size)
        raise
    print_stats(status_codes_stats, total_file_size)


if __name__ == '__main__':
    run()
