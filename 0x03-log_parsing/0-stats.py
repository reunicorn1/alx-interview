#!/usr/bin/python3
"""
This is a script which supplies multiple functions to log parse
"""
import sys


total_size = 0
code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def log(status_code, size):
    """This function logs data from each line of the stimulated HTTP
    GET request for /project/260

    Args:
       status_code (str)
       size (str)
    """
    global total_size
    global code
    total_size += int(size)
    code[int(status_code)] += 1


def flush():
    """This function prints data existing into the stdout in a certain
    format
    """
    global total_size
    global code
    print("File size: {}".format(total_size))
    for key in sorted(code):
        if code[key] == 0:
            pass
        else:
            print("{}: {}".format(key, code[key]))


n = 0
try:
    for line in sys.stdin:
        if len(line.split()) == 9:
            size, status_code = line.split()[8], line.split()[7]
            log(status_code, size)
            n += 1
            if (n % 10 == 0):
                flush()
    flush()
except KeyboardInterrupt as e:
    flush()
    raise e
