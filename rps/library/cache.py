from datetime import timedelta

from redis import Redis

from rps import config


class Cache(object):
    def __init__(self):
        self.redis = Redis(
            host=config.CACHE_HOST,
            port=config.CACHE_PORT,
            username=config.CACHE_USER,
            password=config.CACHE_PASS
        )

    def get_data(self, key_name):
        data = self.redis.get(key_name)
        if data:
            print(f'GET - {key_name}')
            return data
        else:
            return None

    def set_data(self, key_name, expiration_minutes, data):
        print(f'SET - {key_name} - expires in {expiration_minutes} minutes')
        self.redis.setex(
            key_name,
            timedelta(minutes=expiration_minutes),
            value=data
        )

cache = Cache()
