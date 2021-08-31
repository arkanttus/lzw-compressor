from math import ceil

def get_next_char(i, text):
    return text[i+1] if i + 1 < len(text) else ''

def compressor(text):
    last_index = 128
    c_dict = {}
    output_encod = []
    p = ''
    c = ''

    for i, word in enumerate(text):
        if i == 0:
            p = word
            
        c = get_next_char(i, text)
        acc = p + c

        if acc in c_dict:
            p = acc
        else:
            print(word)
            if p in c_dict:
                output_encod.append(c_dict[p])
            else:
                output_encod.append(ord(p))

            c_dict[acc] = last_index
            last_index += 1
            p = c
    
    print(c_dict)
    print(output_encod)
    print(len(output_encod))

    return output_encod

def open_txt():
    with open('tests/01.txt', 'r') as f:
        content = f.read()
    return content

def save(list_encode):
    with open('t1.bin', 'wb') as f:
        for num_code in list_encode:
            f.write(to_byte(num_code))

def to_byte(num):
    b = bin(num)[2:]
    return int.to_bytes(num, ceil(len(b) / 8), 'big')

content = open_txt()
print(content)

list_encode = compressor(content)
save(list_encode)
