# Vigenère Cipher Encryptor and Decryptor

def format_key(message, key):
    key = list(key)
    if len(key) == len(message):
        return "".join(key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(message, key):
    encrypted_text = ""
    key = format_key(message, key)
    
    for i in range(len(message)):
        if message[i].isalpha():
            shift = (ord(message[i].upper()) + ord(key[i].upper())) % 26
            encrypted_char = chr(shift + 65)
            encrypted_text += encrypted_char
        else:
            encrypted_text += message[i]
    return encrypted_text

def decrypt(cipher_text, key):
    decrypted_text = ""
    key = format_key(cipher_text, key)

    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = (ord(cipher_text[i].upper()) - ord(key[i].upper()) + 26) % 26
            decrypted_char = chr(shift + 65)
            decrypted_text += decrypted_char
        else:
            decrypted_text += cipher_text[i]
    return decrypted_text

# Sample run
if __name__ == "__main__":
    print("Vigenère Cipher Encryptor & Decryptor")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()

    if choice == 'E':
        msg = input("Enter the message: ").replace(" ", "").upper()
        k = input("Enter the key: ").upper()
        print("Encrypted Message:", encrypt(msg, k))

    elif choice == 'D':
        cipher = input("Enter the encrypted message: ").replace(" ", "").upper()
        k = input("Enter the key: ").upper()
        print("Decrypted Message:", decrypt(cipher, k))
    else:
        print("Invalid choice.")
