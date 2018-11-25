# coding: utf-8

from hash_util import get_hash
from cache import Cache

class HCache(object):
    def __init__(self, cache_dir):
        self.cache = Cache(cache_dir)

    def get(self, key):
        return self.cache.get(get_hash(key))

    def set(self, key, value):
        self.cache.set(get_hash(key), value)


class UTF8HCache(object):
    def __init__(self, cache_dir):
        self.cache = HCache(cache_dir)

    def get(self, key):
        data = self.cache.get(get_hash(key))
        return data and data.decode('utf-8')

    def set(self, key, value):
        self.cache.set(get_hash(key), value and value.encode('utf-8'))
