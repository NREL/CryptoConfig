import configparser
import os

if __name__ == "__main__":
    try:
        properties = configparser.ConfigParser()
        properties_file = os.path.dirname(__file__) + "/sample_parse.ini"
        properties.read(properties_file)
    
        user = properties.get('PARSE_TEST', 'user')
        password = properties.get('PARSE_TEST', 'password')
    except configparser.ParsingError as err:
        print('Could not parse:', err)

    print(f"user: {user} password: {password}")