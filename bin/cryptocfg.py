#!/usr/bin/env python
#
# command line utility to encode, decode, and generate application keys needed for CryptoConfigParser functionality.

import getopt
import sys

usage = """
use: cryptocfg.py [options]
where options include:
\t--decrypt= | -d, decrypt the string, requires -i and -p 
\t--encrypt= | -e, encrypt the string, requires -i and -p 
\t--input= | -i, string to encrypt or decrypt
\t--password= | -p, key for encrypting or decrypting a string
\t--genkey generate an encryption/decryption string
examples:
Encrypt:
cryptocfg.py -i 'f00Baz!1234$' -p 'jsZ9EkC3_XnP88UwIGQdFWpKPpeaD61RqJy8DE6lLYk=' -e
Decrypt:
cryptocfg.py -i 'gAAAAABa8IpcHE03lpmYYhptWlkOqKMvstpbYlHqp9Asq5qVY024X7OhokVto2aF_uzCRP47OVdHT5VE6f32xIvvoMlDX3_Ceg==' -p 'jsZ9EkC3_XnP88UwIGQdFWpKPpeaD61RqJy8DE6lLYk=' -d
"""

if len(sys.argv) < 2:
    print(usage)
    sys.exit(2)

try:
    from crypto_config import Crypt
except:
    from context import Crypt

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        'degi:o:p:',
        [
            'decrypt',
            'encrypt',
            'genkey',
            'input=',
            'output=',
            'password='
        ])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

#print('OPTIONS   :', options)

encrypt = False
decrypt = False
input_str = None
app_key = None
for opt, arg in options:
    if opt in ('-d', '--decrypt'):
        # call Crypt.decrypt
        decrypt = True
    elif opt in ('-e', '--encrypt'):
        # call Crypt.encrypt
        encrypt = True
    elif opt in ('-g', '--genkey'):
        # call Crypt.gen_key
        print("key: {}".format(Crypt.gen_key()))
        sys.exit(0)
    elif opt in ('-i', '--input'):
        # set input string
        input_str = arg
    elif opt in ('-p', '--password'):
        # set password string from gen_key
        app_key = arg

#print(f"decrypt: {decrypt} encrypt: {encrypt} input_str: {input_str} app_key: {app_key}")

crypt = Crypt(app_key)
if encrypt:
    encrypted = crypt.encrypt(input_str)
    print(f"-----\nunencrypted: {input_str}\nencrypted: {encrypted}\n-----\n")
else:
    decrypted = crypt.decrypt(input_str)
    print(f"-----\nencrypted: {input_str}\ndecrypted: {decrypted}\n-----\n")