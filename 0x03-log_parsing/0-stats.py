#!/usr/bin/env python3
"""This module reads log entries from standard input, processes them line
by line, and computes statistics based on the log data.
"""
import sys
import re
from collections import defaultdict

# Initialize counters
total_size = 0
status_counts = defaultdict(int)
line_count = 0
status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

# Regular expression pattern for line validation
pattern = re.compile(
    r'(?P<ip>\S+) - \[(?P<date>.+?)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)'
)

def print_stats():
    """Print accumulated metrics"""
    print("File size:", total_size)
    for code in sorted(status_codes):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

try:
    # Read from standard input
    for line in sys.stdin:
        match = pattern.match(line)
        if match:
            # Extract status and file size
            status = match.group("status")
            size = int(match.group("size"))
            total_size += size
            if status in status_codes:
                status_counts[status] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats on keyboard interrupt
    print_stats()
    sys.exit()
