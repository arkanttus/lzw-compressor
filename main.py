"""
Terminal args:
1: Path to file that will be compiled
2: Path to where bin file will be saved
"""

from math import ceil
from lzw import LZW
import sys


def open_txt():
    with open(file_to_compress, 'r') as f:
        content = f.read()
    return content


def save(list_encode):
    with open(path_save_bin_file + 't1.bin', 'wb') as f:
        # Get needed bytes to max value in list
        max_value = max(list_encode)
        num_bytes = needed_bytes(max_value)

        # Writing needed bytes in first position of file
        f.write(to_byte(num_bytes, 1))

        # Writing values in list as binary
        for num_code in list_encode:
            byte = to_byte(num_code, num_bytes)
            f.write(byte)


def needed_bytes(num):
    b = bin(num)[2:]
    return ceil(len(b) / 8)


def to_byte(num, num_bytes):
    return int.to_bytes(num, num_bytes, 'big')


# Main
if sys.stdin and sys.stdin.isatty():
    # running in terminal
    if len(sys.argv) >= 3:
        file_to_compress = sys.argv[1] if sys.argv[1] else ''
        path_save_bin_file = sys.argv[2] if sys.argv[2] else ''
    else:
        print(f"Arguments required:\n"
              f"1. Path to file that will be compiled\n"
              f"2. Path to where bin file will be saved")
        exit(1)

content = open_txt()
lzw = LZW()
list_encode = lzw.compressor(content)
save(list_encode)
# print(lzw.decompressor(list_encode))
