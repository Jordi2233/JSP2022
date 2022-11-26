#!/usr/bin/env python3
import os


class cipher:

    def encrypting(writing: str, key: dict) -> str:
        encrypted_writing = ""
        for letter in writing:
            if letter in key:
                letter = key[letter]
                encrypted_writing += letter
            else:
                encrypted_writing += letter
        return encrypted_writing

    def decrypting(writing: str, key: dict):
        encrypted_writing = ""
        for letter in writing:
            if letter in key.values():
                letter = [i for i in key if key[i]==letter]
                letter = ''.join(letter)
                encrypted_writing += letter
            else:
                encrypted_writing += letter
        return encrypted_writing


def main():
    os.system('clear')
    user_str: str = input("Enter the phase: ")
    key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
    # user_str: str = "to jest moj tekst"
    encrypted_text = cipher.encrypting(user_str, key)
    decrypted_text = cipher.decrypting(encrypted_text, key)
    print(encrypted_text)
    print(decrypted_text)


if __name__ == '__main__':
    main()
