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
        f.write(to_byte(num_bytes))

        # Writing values in list as binary
        for num_code in list_encode:
            f.write(to_byte(num_code))

def needed_bytes(num):
    b = bin(num)[2:]
    return ceil(len(b) / 8)

def to_byte(num):
    return int.to_bytes(num, needed_bytes(num), 'big')



# Main

content = open_txt()

lzw = LZW()

list_encode = lzw.compressor(content)
save(list_encode)


lzw.decompressor(list_encode)
