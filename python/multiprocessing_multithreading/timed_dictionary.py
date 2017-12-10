from collections import namedtuple
import time
from threading import Thread, Lock


TimedEntry = namedtuple("TimedEntry", ["value", "expire_at"])


class TimedDictionary(object):
    def __init__(self):
        self._storage = {}
        for i in range(5):
            self._cleaning_thread = Thread(target=self._clean_up, args=(i,))
            self._cleaning_thread.run()
            # time.sleep(1000)

    def _clean_up(self, thread_number):
        print("Running the cleaning process...", thread_number)
        keys = self._storage.keys()
        for key in keys:
            if key in self._storage and self._storage[key].expire_at >= time.time():
                del self._storage[key]
        print("Cleaning process finished...", thread_number)

    def put(self, key, value, expiration):
        self._storage[key] = TimedEntry(value, int(time.time()) + expiration)

    def get(self, key):
        if key not in self._storage:
            return None

        if self._storage[key].expire_at <= time.time():
            del self._storage[key]
            return None
        else:
            return self._storage[key].value


if __name__ == "__main__":
    td = TimedDictionary()
    """
    td.put("GOOGL", 150, 500)
    print(td.get("GOOGL"))
    print(td.get("GOOGL"))
    time.sleep(500)
    td.put("AMZON", 150, 1000)
    print(td.get("GOOGL"))
    print(td.get("GOOGL"))
    print(td)
    print(td.get("AMZON"))
    """

    # del td


