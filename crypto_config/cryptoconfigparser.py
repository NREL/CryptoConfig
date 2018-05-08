from crypto_config import (ConfigParser, ParsingError, Crypt)
import re

class CryptoConfigParser(ConfigParser):

    def __init__(self, *args, **kwargs): 
        key = kwargs.pop('crypt_key', None)
        if key != None:
            self.crypt_key = key
        else:
             self.crypt_key = None
        ConfigParser.__init__(self, *args, **kwargs)

    def get(self, section, option, *args, **kwargs):
        raw_val = ConfigParser.get(self, section, option, *args, **kwargs)
        val = raw_val
        encoded_val = re.search(r"enc\((.*)\)", raw_val, re.IGNORECASE)
        if encoded_val and self.crypt_key:
            val = self._decrypt(encoded_val.group(1), self.crypt_key)
        return val

    def _decrypt(self, str, key):
        c = Crypt(key)
        b_decoded = c.decrypt(str)
        return b_decoded