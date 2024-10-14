from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()

    with open("secret.key","wb") as file:
        file.write(key)

def load_key():
    with open("secret.key","rb") as file:
        key = file.read()
    return key

def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f= Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

generate_key()

# Encrypt a message
original_message = "This is a very informative message!"
encrypted = encrypt_message(original_message)
print(f"Encrypted Message: {encrypted}")

# Decrypt the message
decrypted = decrypt_message(encrypted)
print(f"Decrypted Message: {decrypted}")
    
