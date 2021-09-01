from lzw import LZW

with open('t1.bin', 'rb') as file:
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

    print(arr)

lzw = LZW()

print(lzw.decompressor(arr))