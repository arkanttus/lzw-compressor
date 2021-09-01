from typing import List


class LZW:
    """
    This class implements compressor and decompressor functions using LZW technique.
    """
    def __init__(self) -> None:
        pass
    
    def compressor(self, text) -> List[int]:
        last_idx = 128
        c_dict = {}
        acc = ''
        output_encoded = []

        for word in text:

            if self.in_dict(acc + word, c_dict):
                acc += word
            else:
                code = self.get_code_from_dict(acc, c_dict)
                output_encoded.append(code)
                
                c_dict[acc + word] = last_idx
                last_idx += 1

                acc = word
        
        code = self.get_code_from_dict(acc, c_dict)
        output_encoded.append(code)

        return output_encoded


    def decompressor(self, list_encode) -> str:
        c_dict = {}
        last_idx = 128
        next_code = list_encode[0]
        result = self.translate(next_code, c_dict)
        old_code = next_code

        for code in list_encode[1:]:
            if code in c_dict or code < 128:
                actual_word = self.translate(code, c_dict)

                result += actual_word
                acc = self.translate(old_code, c_dict)

                c_dict[last_idx] = acc + actual_word[0]
                last_idx += 1
            else:
                acc = self.translate(old_code, c_dict)
                new_char = acc + acc[0]
                result += new_char

                c_dict[last_idx] = new_char
                last_idx += 1
            
            old_code = code
        
        return result


    def translate(self, code, c_dict):
        return chr(code) if code < 128 else c_dict[code]


    def in_dict(self, word, dict):
        try:
            return word in dict or ord(word) < 128
        except:
            return False


    def get_code_from_dict(self, word, c_dict):
        return c_dict[word] if word in c_dict else ord(word)


