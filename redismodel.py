import redis
import cipher
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

class PasswordManager(cipher.CipherModel):
    def __init__(self, _port: int, _host: str, _db: int, _password = None, _ssl: bool = False, _salt: int = 16):
        """constructor of the redis manager class

        Args:
            _port (int): port number, eg.: 80
            _host (str): host name, eg.: localhost
            _db (int): database 
            _ssl (bool): if set to True, a secure connection is establish between the client and the server via SSL/TLS
        """
        
        self.redisConnection = redis.Redis(host=_host, port=_port, db=_db, password=_password) ##initalize redis_server 
        self.key = PBKDF2(_password, _salt, 32) 

    def setValue(self, _key: str, _value: str) -> str: 
        """sets key - value pair in the database
            each key should be somewhat unique, if not it will be overwritten by the new one
        Args:
            _key (str): key name
            _value (str): value

        Returns:
            string: returns response message
        """

        try:
            respone = self.redisConnection.set(_key, _value)
            return "Key set properly"

        except redis.exceptions.AuthenticationError:
            return "Authentication failed"

        except redis.exceptions.DataError:
            return "Invalid input"

        except Exception as e:
            return f"Error: {e}"


    def getValue(self, _key: str) -> any:
        """get the value based on the key in the database

        Args:
            _key (str): key name

        Returns:
            any: returns the value if it exists, else nil
        """
        try:
            return self.redisConnection.get(_key)
        
        except redis.exceptions.AuthenticationError:
            return "Authentication failed"

        except redis.exceptions.DataError:
            return "Invalid input"
        
        except Exception as e:
            return f"Error: {e}"
        

    ##deletes value/s based on key/s
    def delValue(self, *args) -> any:
        """method that deletes a values based on given keys from the database
        Args:
            *args can contain bit, string, integer, float
        Returns:
            any: returns 1 if deleted 0 if key doesnt exist and string error message
        """

        _keys = [arg for arg in args]

        try:
            return self.redisConnection.delete(*_keys)

        except redis.exceptions.AuthenticationError:
            return "Authentication failed"

        except redis.exceptions.DataError:
            return "Invalid input"
        
        except Exception as e:
            return f"Error: {e}"
    
    def setHash(self, _key: str, _value: str) -> str:
        """sets hash value based on a key to redis in a particular order

        Args:
            _key (str): key name
            _value: string describing your password

        Returns:
            str: returns response string
        """
        pw, nonce, tag = self.encrypt(_value)

        try:
            self.redisConnection.hset(_key, "pw", pw)
            self.redisConnection.hset(_key, "nonce", nonce)
            self.redisConnection.hset(_key, "tag", tag)
            return "OK"
        
        except redis.exceptions.AuthenticationError:
            return "Authentication failed"
        
        except redis.exceptions.DataError:
            return "Invalid input"
        
        except Exception as e:
            return f"Error: {e}"
        

    def getHash(self, _key: str) -> dict:
        """returns hash values based on key from redis database

        Args:
            _key (str): key name

        Returns:
            dict: returns a dictionary
        """

        try:
            encData = self.redisConnection.hgetall(_key)
            return self.decrypt(encData)


        except redis.exceptions.AuthenticationError:
            return "Authentication failed"
        
        except redis.exceptions.DataError:
            return "Invalid input"
        
        except Exception as e:
            return f"Error: {e}"
