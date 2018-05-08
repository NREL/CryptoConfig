import unittest
from context import Crypt

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.my_string = 'this is my string to encrypt.'
        key = Crypt.gen_key()
        self.c = Crypt(key)
        self.encrypted = self.c.encrypt(self.my_string)

    def test_encrypt(self):
        self.assertIsNot(self.encrypted, None, msg="encryption assertion failed!")

    def test_decrypt(self):
        # crypt returns byte encoded string so decode before asssertion!
        decrypted = self.c.decrypt(self.encrypted)
        self.assertEqual(decrypted, self.my_string, msg="decryption assertion failed!")

if __name__ == '__main__':
    unittest.main()