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
    group1 = r'^(\d{0,3}.){3}\d{0,3} - '
    group2 = r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2}).(\d{6})\] '
    group3 = r'"GET \/projects\/260 HTTP\/1.1" [1-5]0[0-5] (\d{0,4})$'
    regex = group1 + '|' + group2 + '|' + group3
    form = re.compile(regex)
    if form.search(line):
        return True
    return False


def print_log():
    """
    This function prints the statistics from input read so format
    """
    global file_size
    global status_code
    print('File size:', file_size)
    keys = sorted(list(status_code.keys()))
    for key in keys:
        if not status_code[key]:
            continue
        print('{}: {}'.format(key, status_code[key]))


def processer(line):
    """
    This is the main engine which process the lines and increment

    Parameters:
    ----------
    line: str
        The processed line
    """
    global file_size
    global status_code
    regex_filesize = re.compile('[0-9]{0,3}$')
    regex_status = re.compile('[1-5]0[0-5](?= [0-9]{0,4}$)')
    file_size += int(regex_filesize.search(line).group())
    status = int(regex_status.search(line).group())
    status_code[status] += 1


def handle_signal(signum, frame):
    """
    This function handles ctrl+C signal to execute print_log function
    """
    print_log()


def main():
    """
    The entry point of the app
    """
    signal.signal(signal.SIGINT, handle_signal)
    count = 0
    while sys.stdin.readline():
        line = sys.stdin.readline().strip()
        count += 1
        if regex(line):
            processer(line)
        if (count % 10 == 0):
            print_log()


if __name__ == '__main__':
    main()
