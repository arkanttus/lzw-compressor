"""
Terminal args:
1: Operation 'encode' or 'decode'
1: Path to file that will be compiled
2: Path to where bin file will be saved
"""

from math import ceil
from lzw import LZW
from utils import open_txt, open_bin, save_bin, save_txt

import sys
import os


# Main
if sys.stdin and sys.stdin.isatty():
    # running in terminal

    if len(sys.argv) > 1:
        operation = sys.argv[1]
        if operation not in ['encode', 'decode']:
            # Check if operation is valid
            print("The operation must be 'encode' or 'decode'")
    else:
        print(f"Arguments required:\n"
              f"1. The operation ('encode' or 'decode')\n"
              f"2. Path to file that will be compiled\n"
              f"3. Path to where bin file will be saved")
        exit(1)

    if operation == 'encode':
        if len(sys.argv) >= 3:
            file_to_compress = sys.argv[2] if sys.argv[2] else ''
            path_save_bin_file = sys.argv[3] if sys.argv[3] else ''

            if not os.path.isfile(file_to_compress):
                # Check if file exists
                print("The txt file does not exists")
                exit(1)

            if file_to_compress.split("/")[-1].split(".")[1] != "txt":
                # Check if file to compress is a .txt
                print("The file must be a .txt")
                exit(1)

            if not os.path.exists('/'.join(path_save_bin_file.split("/")[0:-1])):
                # Check if path to save file exists
                print("The path to save bin file does not exists")
                exit(1)

            if path_save_bin_file.split("/")[-1].split(".")[1] != "bin":
                # Check if file to save is a .bin
                print("The file to save must be a .bin")
                exit(1)

        else:
            print(f"Arguments required:\n"
                  f"1. The operation ('encode' or 'decode')\n"
                  f"2. Path to file that will be compiled\n"
                  f"3. Path to where bin file will be saved")
            exit(1)

    elif operation == 'decode':
        if len(sys.argv) >= 3:
            path_to_bin_file = sys.argv[2] if sys.argv[2] else ''
            path_to_save_txt_file = sys.argv[3] if sys.argv[3] else ''

            if not os.path.isfile(path_to_bin_file):
                # Check if file exists
                print("The bin file does not exists")
                exit(1)

            if path_to_bin_file.split("/")[-1].split(".")[1] != "bin":
                # Check if file to save is a .bin
                print("The file to save must be a .bin")
                exit(1)

            if not os.path.exists('/'.join(path_to_save_txt_file.split("/")[0:-1])):
                # Check if path to save txt file exists
                print("The path to save txt file does not exists")
                exit(1)

            if path_to_save_txt_file.split("/")[-1].split(".")[1] != "txt":
                # Check if file to save is a .bin
                print("The file to save must be a .txt")
                exit(1)
        else:
            print(f"Arguments required:\n"
                  f"1. The operation ('encode' or 'decode')\n"
                  f"2. Path to bin file\n"
                  f"3. Path to where txt file will be saved")

lzw = LZW()
if operation == 'encode':
    content = open_txt(file_to_compress)
    list_encode = lzw.compressor(content)
    save_bin(list_encode)
elif operation == 'decode':
    list_encode = open_bin(path_to_bin_file)
    content = lzw.decompressor(list_encode)
    save_txt(path_to_save_txt_file, content)
else:
    print('Invalid operation')
    exit(1)

print('Done!')

# print(lzw.decompressor(list_encode))
