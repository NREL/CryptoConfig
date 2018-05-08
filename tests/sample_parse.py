from context import crypto_config
from crypto_config import cryptoconfigparser
import os

if __name__ == "__main__":
    try:
        # CryptoConfigParser application encrypton string
        key = '-nBUOebi1SsnpU8k7lHym6oHSFN5Id3xM0Wezh8DHxg='

        properties = cryptoconfigparser.CryptoConfigParser(crypt_key=key)
        #properties = cryptoconfigparser.CryptoConfigParser()
        properties_file = os.path.dirname(__file__) + "/sample_parse.ini"
        properties.read(properties_file)
    
        user = properties.get('PARSE_TEST', 'user')
        password = properties.get('PARSE_TEST', 'password')
        password_encoded = properties.get('PARSE_TEST', 'password_encoded')
    except cryptoconfigparser.ParsingError as err:
        print('Could not parse:', err)

    print(f"user: {user} password: {password} decoded: {password_encoded}")
