
def needed_bytes(num):
    b = bin(num)[2:]
    return ceil(len(b) / 8)


def to_byte(num, num_bytes):
    return int.to_bytes(num, num_bytes, 'big')


def open_txt(file_to_compress):
    with open(file_to_compress, 'r') as f:
        content = f.read()
    return content


def open_bin(file):
    with open(file, 'rb') as file:
        byte_length = int.from_bytes(file.read(1), byteorder='big')
        # file.seek(1)
        # print(byte_length)
        arr = list()

        while True:
            byte = file.read(byte_length)

            if byte != b'':
                arr.append(int.from_bytes(byte, 'big'))
            else:
                break

        return arr


def save_bin(list_encode):
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
