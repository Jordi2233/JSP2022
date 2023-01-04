def caesar_cipher(string, key):
    result = ""

    for char in string:
        if char.isalpha():
            char = chr(ord(char) + key)

            if not char.isalpha():
                char = chr(ord(char) - 26)

        result += char

    return result
