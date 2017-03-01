#!/usr/bin/env python
# encoding: utf-8

import threading

class Singleton(object):
    Instance = None

    lock = threading.RLock()

    def __new__(cls):
        cls.lock.acquire()
        if cls.Instance is None:
            cls.Instance = super(Singleton, cls).__new__(cls)
        cls.lock.release()
        return cls.Instance

if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    print id(a)
    print id(b)
    assert id(a) == id(b)