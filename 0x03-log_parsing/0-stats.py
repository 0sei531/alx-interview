#!/usr/bin/python3
'''A script for parsing HTTP request logs.'''
import re
import sys


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.'''
    pattern = (
        r'\s*(?P<ip>\S+)\s*'
        r'\s*\[(?P<date>[^\]]+)\]'
        r'\s*"(?P<request>[^"]*)"\s*'
        r'\s*(?P<status_code>\d+)'
        r'\s*(?P<file_size>\d+)'
    )
    match = re.match(pattern, input_line)
    if match:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size')),
        }
    return {'status_code': 0, 'file_size': 0}


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.'''
    print(f'File size: {total_file_size}', flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats[status_code]
        if count > 0:
            print(f'{status_code}: {count}', flush=True)

def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.'''
    line_info = extract_input(line)
    status_code = line_info['status_code']
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']

def run():
    '''Starts the log parser.'''
    total_file_size = 0
    status_codes_stats = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    line_num = 0

    try:
        for line in sys.stdin:
            total_file_size = update_metrics(line.strip(), total_file_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)
        raise

if __name__ == '__main__':
    run()
