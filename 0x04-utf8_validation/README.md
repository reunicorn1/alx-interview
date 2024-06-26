# 0x04. UTF-8 Validation

UTF-8 is a variable-width character encoding used for electronic communication. It is capable of encoding all possible characters, or code points, defined by Unicode. The encoding is variable-width, as code points are encoded with one to four 8-bit bytes.
In UTF-8, each byte of a character begins with a unique binary pattern. This pattern helps identify whether the byte is a single byte character, one of the leading bytes (in a multi-byte character), a continuation byte, or an invalid byte.
Single byte characters (ASCII characters) start with '0'.
Leading bytes start with '11'.
Continuation bytes start with '10'.
To validate a sequence of bytes as UTF-8, you would check these patterns and also ensure that each multi-byte character has the correct number of continuation bytes following its leading byte.


## 0. UTF-8 Validation
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

