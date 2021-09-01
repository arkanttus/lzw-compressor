with open('t1.bin', 'rb') as file:
    byte_length = int.from_bytes(file.read(1), byteorder='big')
    print(byte_length)
    arr = list()

    a = int.to_bytes(10, 2, byteorder='big')
    print(a)
    print(int.from_bytes(a, byteorder='big'))

    while True:
        byte = file.read(byte_length)

        if byte != b'':
            print(byte)
            arr.append(int.from_bytes(byte, byteorder='big'))
        else:
            break

    print(arr)
