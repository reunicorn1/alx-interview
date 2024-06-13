#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 0
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 2
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 8
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


n = 32
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


n = 16
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1001
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

