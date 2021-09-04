from math import ceil

"""
Return needed bytes to represent a number
"""
def needed_bytes(num):
    b = bin(num)[2:]
    return ceil(len(b) / 8)

"""
Return a number in bytes
"""
def to_byte(num, num_bytes):
    return int.to_bytes(num, num_bytes, 'big')


def open_txt(file_to_compress):
    with open(file_to_compress, 'r') as f:
        content = f.read()
    return content

"""
Open a bin file and convert to a list of integers
"""
def open_bin(file):
    with open(file, 'rb') as file:
        byte_length = int.from_bytes(file.read(1), byteorder='big')
        arr = []

        while True:
            byte = file.read(byte_length)

            if byte != b'':
                arr.append(int.from_bytes(byte, 'big'))
            else:
                break

        return arr

"""
Receive a list of integers, transform this list in bytes and save into file
"""
def save_bin(list_encode, path_save_bin_file):
    with open(path_save_bin_file, 'wb') as f:
        # Get needed bytes to max value in list
        max_value = max(list_encode)
        num_bytes = needed_bytes(max_value)

        # Writing needed bytes in first position of file
        f.write(to_byte(num_bytes, 1))

        # Writing values in list as binary
        for num_code in list_encode:
            byte = to_byte(num_code, num_bytes)
            f.write(byte)


def save_txt(file, content):
    with open(file, 'w') as f:
        f.write(content)
