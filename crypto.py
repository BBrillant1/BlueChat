from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
def encrypt_message(msg):
    return cipher.encrypt(msg.encode())
def decrypt_message(encrypted):
    return cipher.decrypt(encrypted).decode()