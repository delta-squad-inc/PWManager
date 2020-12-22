from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import string
import secrets


class CipherModel:
    def __init__(self, _password: str, _salt: int = 16):
        
        print(_password)
        self.key = PBKDF2(_password, _salt, 32)
    
    def encrypt(self, data: str) -> tuple:
        """encrypts string value with AES

        Args:
            data (str): usually the string you want to encrypt for example: pw123456

        Returns:
            tuple: returns the ciphertext, nonce and tag in that order as a tuple
        """

        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
        return ciphertext, cipher.nonce, tag

    def decrypt(self, encdata: dict) -> str:
        """decrypts a string value based on other attributes such as tag and data

        Args:
            encdata (dict): encrypt dictionary that contains the string, nonce and tag

        Returns:
            str: returns plaintext if verified, else returns Error message.
        """
        
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=encdata[b'nonce'])
        plaintext = cipher.decrypt(encdata[b'pw'])

        try:
            cipher.verify(encdata[b'tag'])
            return plaintext.decode()
        except ValueError:
            return "Incorrect key or corrupted message"
    
    def generatepassword(self, length: int = 22) -> str:
        """Method that generates a random sequence of strings

        Args:
            length (int, optional): Return string length. Defaults to 16.

        Returns:
            str: randomly generated string
        """
        password = ''.join(secrets.choice(string.ascii_letters + string.digits+'$_-') for i in range(length))
        return password



