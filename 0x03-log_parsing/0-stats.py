#!/usr/bin/python3
"""
0. Log parsing
"""
import re
import signal
import sys

file_size = 0
status_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def regex(line):
    """
    This function checks the line format and if it matches the specificed
    format it returns true otherwise false

    Parameters:
    ----------
    line: str
        The line from stdin

    Returns:
    -------
        Either true or false if it matches format or not
    """
    log_pattern = re.compile(
            r'^\d{1,3}(\.\d{1,3}){3} - '
            r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
            r'"GET \/projects\/260 HTTP\/1.1" ([1-5]0[0-5]) (\d+)$'
    )
    return log_pattern.search(line)


def print_log():
    """
    This function prints the statistics from input read
    """
    global file_size
    global status_code
    print('File size:', file_size)
    for key in sorted(list(status_code.keys())):
        if status_code[key]:
            print('{}: {}'.format(key, status_code[key]))


def processer(line):
    """
    This is the main engine which process the lines read

    Parameters:
    ----------
    line: str
        The processed line
    """
    global file_size
    global status_code
    file_size += int(line.split()[-1])
    status = int(line.split()[-2])
    status_code[status] += 1


def handle_signal(signum, frame):
    """
    This function handles ctrl+C signal to execute print_log function

    signum: Callable object
    frame: Dataframe object
    """
    print_log()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_signal)


def main():
    """
    The entry point of the app
    """
    count = 0
    for line in sys.stdin:
        count += 1
        if regex(line):
            processer(line)
        if (count % 10 == 0):
            print_log()


if __name__ == '__main__':
    main()
