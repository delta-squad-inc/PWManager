import redis
import sys
import logging

class redisManager(object):
    def __init__(self, _port: int, _host: str, _db: int):
        ##initalize redis_server 
        self.redisConnection = redis.Redis(host=_host, port=_port, db=_db)

        ##set key/value indefinitely
    def setValue(self, _key: str, _value: str) -> bool: 
        ##returns False 
        return self.redisConnection.set(_key, _value)

    ##get value based on key
    def getValue(self, _key: str) -> any:
        ##returns value, or (nil) if key doesn't exist
        return self.redisConnection.get(_key)

    ##deletes value/s based on key/s
    def deleteValue(self, _keys: list) -> any:
        #if no key is given return with warning, else continue
        if len(_keys) == 0:
            return "Missing keys, 0 given"
        return self.redisConnection.delete(*_keys)

def main() -> None: 
    Manager = redisManager(6379, 'localhost', 0)
    #Redis.setValue('password', 'pw12345')
    #response = Manager.deleteValue([1, 2])
    #print(f"Response is: {response}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f'The program will abort due to exception {e}. Exception was logged.', exc_info=True)
        sys.exit(0)    
