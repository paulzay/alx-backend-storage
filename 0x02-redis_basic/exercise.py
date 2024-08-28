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
