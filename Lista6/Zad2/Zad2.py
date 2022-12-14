#!/usr/bin/env python3
import os
from cipher import caesar_cipher


def main():
    os.system('clear')

    encrypted_string = caesar_cipher("hello", 3)
    decrypted_string = caesar_cipher(encrypted_string, -3)

    print(f'Encrypted string: {encrypted_string}')
    print(f'Decrypted string: {decrypted_string}')


if __name__ == '__main__':
    main()
