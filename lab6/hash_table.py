import hashlib
from typing import List, Optional


class Node:
    def __init__(self, key: Optional[str], data):
        self.key: Optional[str] = key
        self.data = data


class HashTable:
    def __init__(self):
        self.__table: List[Node] = [Node(None, 0) for _ in range(20)]
        self.table_size = 20
        self.inserted_elements = 0
        self.resize_multiplier = 2
        self.resize_threshold = 0.5

    def add(self, key: str, data):
        if key == "":
            return

        try_count = 0
        pos = self._get_pos(key, try_count)
        while self.__table[pos].key is not None:
            try_count += 1
            pos = self._get_pos(key, try_count)

        self.inserted_elements += 1
        self.__table[pos] = Node(key, data)
        self.check_resize()

    def get(self, key: str):
        if key == "":
            return

        try_count = 0
        pos = self._get_pos(key, try_count)
        if self.__table[pos].key is None:
            return
        while self.__table[pos].key != key:
            if self.__table[pos].key is None:
                return
            try_count += 1
            pos = self._get_pos(key, try_count)

        return self.__table[pos].data

    def remove(self, key: str):
        if key == "":
            return

        try_count = 0
        pos = self._get_pos(key, try_count)
        if self.__table[pos].key is None:
            return
        while self.__table[pos].key != key:
            if self.__table[pos].key is None:
                return
            try_count += 1
            pos = self._get_pos(key, try_count)

        self.inserted_elements -= 1
        self.__table[pos] = Node(None, 0)

    def update(self, key: str, new_data):
        if key == "":
            return

        try_count = 0
        pos = self._get_pos(key, try_count)
        while self.__table[pos].key != key:
            try_count += 1
            pos = self._get_pos(key, try_count)
        self.__table[pos] = Node(key, new_data)

    def _first_hash(self, key: str) -> int:
        return int(hashlib.sha1(key.encode("utf-8")).hexdigest(), 16) % (10**8)

    def _second_hash(self, key: str) -> int:
        return int(hashlib.sha512((key + "A").encode("utf-8")).hexdigest(), 16) % (10**8)

    def _get_pos(self, key: str, try_count: int) -> int:
        pos = (
            self._first_hash(key) + try_count * self._second_hash(key)
        ) % self.table_size
        return pos

    def check_resize(self):
        if (self.inserted_elements / self.table_size) >= self.resize_threshold:
            self._resize_table()

    def _add(self, key: str, data):
        if key == "":
            return

        try_count = 0
        pos = self._get_pos(key, try_count)
        while self.__table[pos].key is not None:
            try_count += 1
            pos = self._get_pos(key, try_count)

        self.__table[pos] = Node(key, data)
        self.check_resize()

    def _resize_table(self):
        old_table = self.__table
        self.table_size *= self.resize_multiplier
        self.__table = [Node(None, 0) for _ in range(self.table_size)]

        for elem in old_table:
            if elem.key is not None:
                self._add(elem.key, elem.data)
