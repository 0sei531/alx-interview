# 0x03. Log Parsing

## Description
This project involves reading from standard input, processing log entries in real-time, and computing specific metrics based on the input data. The script processes log entries in a given format, aggregates data, and prints statistics periodically or upon keyboard interruption (CTRL + C).

## Concepts
- **File I/O in Python**
  - Reading from `sys.stdin` line by line.
- **Signal Handling in Python**
  - Handling keyboard interruption (CTRL + C) using signal handling in Python.
- **Data Processing**
  - Parsing strings to extract specific data points.
  - Aggregating data to compute summaries.
- **Regular Expressions**
  - Using regular expressions to validate the format of each line.
- **Dictionaries in Python**
  - Using dictionaries to count occurrences of status codes and accumulate file sizes.
- **Exception Handling**
  - Handling possible exceptions that may arise during file reading and data processing.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable
- The length of files will be tested using `wc`

## Task
### 0. Log parsing
- Write a script that reads from `stdin` line by line and computes metrics.
- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
  - If the format is not this one, the line must be skipped.
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
  - Total file size: `File size: <total size>` where `<total size>` is the sum of all previous `<file size>`
  - Number of lines by status code:
    - Possible status codes: 200, 301, 400, 401, 403, 404, 405, 500
    - Format: `<status code>: <number>`
    - Status codes should be printed in ascending order

## Example
```sh
alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
    for line in sys.stdin:
KeyboardInterrupt
  File "./0-generator.py", line 8, in <module>
    sleep(random.random())
KeyboardInterrupt
alexa@ubuntu:~/0x03-log_parsing$ 
