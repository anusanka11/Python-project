def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            result += encrypted_char
        else:
            result += char
    return result

# To decrypt a message, you can use the same function with a negative shift value
def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

# Enter Data:
message = str(input('Entrt the Message = '))
key = int(input('Enter the Shift Key = '))

encrypted_message = caesar_cipher(message, key)
decrypted_message = caesar_decipher(encrypted_message, key)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
