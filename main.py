"""
Terminal args:
1: Operation 'encode' or 'decode'
1: Path to file that will be compiled
2: Path to where bin file will be saved
"""

from math import ceil
from lzw import LZW
from file_utils import open_txt, open_bin, save_bin, save_txt
from args_utils import get_args


# Main

operation, path_to_read, path_to_save = get_args()

lzw = LZW()

if operation == 'encode':
    content = open_txt(path_to_read)
    list_encode = lzw.compressor(content)
    save_bin(list_encode, path_to_save)

elif operation == 'decode':
    list_encode = open_bin(path_to_read)
    content = lzw.decompressor(list_encode)
    save_txt(path_to_save, content)

print('Done!')