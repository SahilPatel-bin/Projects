Project Describe:-

This project demonstrates how to securely encrypt and decrypt sensitive information using Python and the cryptography library. The system employs symmetric encryption through the Fernet module, which guarantees message confidentiality. The project involves key generation, secure message encryption, and decryption.

Functionality:
1) Key Generation: A cryptographic key is generated once and saved to a file. This key is required for both encrypting and decrypting messages. It ensures that the data can only be decrypted by someone who possesses the key.

2) Message Encryption: The system takes a plain text message, converts it into a byte format, and encrypts it using the generated key. This encryption ensures that the message remains secure and cannot be understood by unauthorized users.

3) Message Decryption: After encryption, the system can decrypt the message back to its original form using the same key. The process is seamless and demonstrates how encryption systems can protect sensitive data.
