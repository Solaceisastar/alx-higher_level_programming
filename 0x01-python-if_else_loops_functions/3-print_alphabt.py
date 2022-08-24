#!/usr/bin/python3
for ascii in range(97, 123):
    if chr(ascii) != 'q' and chr(ascii) != 'e':
        print("{}".format(chr(ascii)), end="")
