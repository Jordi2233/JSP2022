def caesar_cipher(string, key):
  # Create an empty result string
  result = ""

  # Loop through each character in the string
  for char in string:
    # If the character is a letter (uppercase or lowercase)
    if char.isalpha():
      # Shift the character by the key amount
      char = chr(ord(char) + key)
      
      # If the shifted character is not a letter,
      # subtract 26 to "wrap" it back into the alphabet
      if not char.isalpha():
        char = chr(ord(char) - 26)

    # Add the shifted character to the result string
    result += char

  # Return the result string
  return result
