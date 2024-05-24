import unittest
from hash_table import HashTable


class Table1(unittest.TestCase):
    def setUp(self):
        self.t = HashTable()
        for i in range(120):
            self.t.add(str(i), i)

    def test_get(self):
        self.assertEqual(self.t.get("1"), 1)

    def test_size(self):
        self.assertEqual(self.t.table_size, 320)

    def test_remove(self):
        self.t.remove("3")
        self.t.remove("6")
        self.assertEqual(self.t.get("3"), None)

    def test_remove2(self):
        self.t.remove("3")
        self.t.remove("6")
        self.t.add("3", 110)
        self.assertEqual(self.t.get("3"), 110)

    def test_update(self):
        self.t.update("3", 120)
        self.assertEqual(self.t.get("3"), 120)

    def test_get2(self):
        self.assertEqual(self.t.get(""), None)

    def test_remove3(self):
        self.t.remove("")
        self.assertEqual(self.t.get(""), None)

    def test_get3(self):
        self.assertEqual(self.t.get("97"), 97)

    def test_get_empty(self):
        self.assertEqual(self.t.get(""), None)

    def test_remove_empty(self):
        self.assertEqual(self.t.remove(""), None)

    def test_update_empty(self):
        self.assertEqual(self.t.update("", ""), None)


if __name__ == "__main__":
    unittest.main()
