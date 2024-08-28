#!/usr/bin/env python3
""" redis basic exercise """
import redis
import uuid
from typing import Union


class Cache():
    """ cache class definition """

    def __init__(self) -> None:
        """initialize values"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store key and data """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key, fn):
        """ get key and data """
        value = self._redis.get(key)
        if value:
            return fn(value)
        return None

    def get_str(self, key: str) -> str:
        """ get string"""
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """ get int"""
        return self.get(key, fn=int)