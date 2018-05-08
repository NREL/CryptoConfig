import unittest
import os
from context import crypto_config
from crypto_config import cryptoconfigparser

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        try:
            self.key = '-nBUOebi1SsnpU8k7lHym6oHSFN5Id3xM0Wezh8DHxg='
            self.properties = cryptoconfigparser.CryptoConfigParser(crypt_key=self.key)
            properties_file = os.path.dirname(__file__) + "/sample_parse.ini"
            self.properties.read(properties_file)
        except cryptoconfigparser.ParsingError as err:
            print('Could not parse:', err)

    def test_no_encrypted_get(self):
        user = self.properties.get('PARSE_TEST', 'user')
        self.assertEqual(user, 'dmartin', msg="non encrypted get assertion failed!")
    
    def test_encrypted_get(self):
        password = self.properties.get('PARSE_TEST', 'password')
        password_encoded = self.properties.get('PARSE_TEST', 'password_encoded')
        self.assertEqual(password, password_encoded, msg="password decode assertion failed!")

if __name__ == '__main__':
    unittest.main()