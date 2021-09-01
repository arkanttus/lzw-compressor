from math import ceil
from lzw import LZW


def open_txt():
    with open('tests/01.txt', 'r') as f:
        content = f.read()
    return content

def save(list_encode):
    with open('t1.bin', 'wb') as f:        
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

content = open_txt()

lzw = LZW()

list_encode = lzw.compressor(content)
save(list_encode)

print(lzw.decompressor(list_encode))
