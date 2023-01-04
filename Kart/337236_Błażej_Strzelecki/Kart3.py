import os
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL_CHARS = " ,.-;:_?!=łążźćńóęąśŁĄŻŹĆŃÓĘĄŚ123456789"


def decrypt(cipher_text, key=None):

    plain_text = ""
    for letter in cipher_text:
        if letter in SPECIAL_CHARS:
            plain_text += letter
            continue
        index = ALPHABET.find(letter.upper())
        new_index = flatten(index - key)
        plain_text += ALPHABET[new_index]

    return plain_text


def flatten(number):
    """
    Flattens the key back to be in range(1,26)
    :param number: 
    :return: 
    """
    return number - (26*(number//26))



def main():

    file_path = f'{os.path.dirname(__file__)}/payload_337236.txt'

    with open(file_path, "r+", encoding="UTF-8") as f:
        secret = [line.rstrip() for line in f]

    secret = "".join(secret)
    for i in range(0, 26):
        key =  i
        encoded = decrypt(secret, key)
        if ("BłAżEJ" in encoded) and ("STRZELECKI" in encoded) and ("337236" in encoded):
            res = f"Key: {key} \n {encoded}"
            break

    with open("output.txt", "w+", encoding="UTF-8") as f:
        f.write(res)
if __name__ == '__main__':
    main()
