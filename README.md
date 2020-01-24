# cryptoconfig 
## Python class for handling encrypted elements in a config file.  Extension of [ConfigParser](https://docs.python.org/3/library/configparser.html 'ConfigParser').
### This class overides the 'get' method of ConfigParser replacing it with [Fernet](https://cryptography.io/en/latest/fernet/ 'Fernet') symmetric encryption so that you can safely store encrypted passwords in an ini file.
### Example ini file.
```
[PARSE_TEST]
user = dmartin
password = ba$1234!
password_encoded = enc(gAAAAABa7JOds0uLwiKb44pTUvLuzbcxLsmpWL7kCFYTKX0JTW6q_JLubSKFrecCF1ShsMvzEBnt16Da_LsgUN5ff5LwB6zwPw==)
```
### Example code to parse the above ini example.  Note: The encoded password is the same as the unencoded to demonstrate the use.  Storing the crypt_key in the program should be discouraged.  A better example would load the key from an environment variable.
```
from crypto_config import cryptoconfigparser
import os
import sys

if __name__ == "__main__":
    try:
        # CryptoConfigParser application encrypton string
        key = '-nBUOebi1SsnpU8k7lHym6oHSFN5Id3xM0Wezh8DHxg='

        properties = cryptoconfigparser.CryptoConfigParser(crypt_key=key)
        properties_file = os.path.dirname(__file__) + "/sample_parse.ini"
        properties.read(properties_file)
    
        user = properties.get('PARSE_TEST', 'user')
        password = properties.get('PARSE_TEST', 'password')
        password_encoded = properties.get('PARSE_TEST', 'password_encoded')
    except cryptoconfigparser.ParsingError as err:
        print('Could not parse:', err)
        sys.exit(1)

    print(f"user: {user} password: {password} decoded: {password_encoded}")

```
### To install this from git use:
```
pip install git+https://github.com/NREL/CryptoConfig.git
```
### This package installs a helper command line utility called cryptocfg.py to generate, encrypt, and decrypt Fernet password strings.
```
use: cryptocfg.py [options]
where options include:
	--decrypt= | -d, decrypt the string, requires -i and -p 
	--encrypt= | -e, encrypt the string, requires -i and -p 
	--input= | -i, string to encrypt or decrypt
	--password= | -p, key for encrypting or decrypting a string
	--genkey generate an encryption/decryption string
examples:
Encrypt:
cryptocfg.py -i 'f00Baz!1234$' -p 'jsZ9EkC3_XnP88UwIGQdFWpKPpeaD61RqJy8DE6lLYk=' -e
Decrypt:
cryptocfg.py -i 'gAAAAABa8IpcHE03lpmYYhptWlkOqKMvstpbYlHqp9Asq5qVY024X7OhokVto2aF_uzCRP47OVdHT5VE6f32xIvvoMlDX3_Ceg==' -p 'jsZ9EkC3_XnP88UwIGQdFWpKPpeaD61RqJy8DE6lLYk=' -d
```
