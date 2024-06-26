#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

print('-----------------')

data = [0x24, 0x61, 0x7A]
print(validUTF8(data))

data = [0xC3, 0xA9]
print(validUTF8(data))

data = [0xE2, 0x82, 0xAC]
print(validUTF8(data))

data = [0xF0, 0x9F, 0x98, 0x80]
print(validUTF8(data))

data = [0x24, 0xC2, 0xA2, 0xE2, 0x82, 0xAC, 0xF0, 0x9F, 0x98, 0x80]
print(validUTF8(data))

data = [0xC3, 0x28]
print(validUTF8(data))

data = [0xE2, 0x82]
print(validUTF8(data))

print('-----------------')

data = [0xC0, 0x80]
print(validUTF8(data))

data = [0xC3, 0xA9, 0x80]
print(validUTF8(data))

data = []
print(validUTF8(data))


print(80 & 192)
