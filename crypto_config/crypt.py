from cryptography.fernet import Fernet

class Crypt(object):
    
    def __init__(self, password):
        """
        Crypt constructor
            :param password: byte encoded string.
        """ 
        try:
            p = password.encode()
        except AttributeError:
            p = password

        self.cipher = Fernet(p)
        
    def decrypt(self, s):
        """
        Decrypt a string
            :param s: string to decrypt
        """ 
        try:
            encrypted_str = s.encode()
        except AttributeError:
            encrypted_str = s

        decrypted = self.cipher.decrypt(encrypted_str)
        return decrypted.decode()


    def encrypt(self, s):
        """
        Encrypt a string
            :param s: string to encrypt
        """   
        try:
            encoded_str = s.encode()
        except AttributeError:
            encoded_str = s
        return self.cipher.encrypt(encoded_str).decode()

    @staticmethod
    def gen_key():
        """
        Generates a fresh fernet key. Keep this some place safe! 
        """   
        key = Fernet.generate_key()
        return key.decode()
        
