from collections import namedtuple
import time


def get_epoch_time():
    return int(time.time())


DictWEEntry = namedtuple("DictWEEntry", ["value", "expiration"])


class DictWithExpiration(object):
    def __init__(self):
        self.storage = {}

    @property
    def size(self):
        return len(self.storage)

    def empty(self):
        return self.size == 0

    def get(self, key, default=None):
        if key not in self.storage or \
                (self.storage[key] and self.storage[key].expiration < get_epoch_time()):
            del self.storage[key]
            return default

        return self.storage[key].value

    def put(self, key, value, duration):
        if type(duration) != int:
            raise TypeError(
                "duration is a(n) {} instead of an int".format(type(duration))
            )

        if duration <= 0:
            raise ValueError(
                "duration cannot be zero or negative"
            )

        self.storage[key] = DictWEEntry(value, duration + get_epoch_time())
