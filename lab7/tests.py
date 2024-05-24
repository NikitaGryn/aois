import unittest
from Matrix import Matrix


class Matrix1(unittest.TestCase):
    def setUp(self):
        self.m = Matrix()
        self.m.set_word(0, "0100011000101000")
        self.m.set_word(1, "0100000100101000")
        self.m.set_word(2, "0010000100101000")
        self.m.set_word(3, "0001011100101000")
        self.m.set_word(4, "0100011100101000")
        self.m.set_word(5, "0101011100101000")
        self.m.set_word(6, "0000011100101000")
        self.m.set_word(7, "0101110100101000")
        self.m.set_word(8, "0001011000100000")
        self.m.set_word(9, "0100111100101000")
        self.m.set_word(10, "0100011100101000")
        self.m.set_word(11, "0001111100101000")
        self.m.set_word(12, "0100011100101000")
        self.m.set_word(13, "0001011100101000")
        self.m.set_word(14, "0000111100101000")
        self.m.set_word(15, "0100011100101000")

    def test_max(self):
        self.assertEqual(1, self.m.nearest_max("0100000000000000"))

    def test_min(self):
        self.assertEqual(2, self.m.nearest_min("0100000000000000"))


class Matrix2(unittest.TestCase):
    def setUp(self):
        self.m = Matrix()
        self.m.set_word(0, "0100011000101000")
        self.m.set_word(1, "0100000100101000")
        self.m.set_word(2, "0010000100101000")
        self.m.set_word(3, "0001011100101000")
        self.m.set_word(4, "0100011100101000")
        self.m.set_word(5, "0101011100101000")
        self.m.set_word(6, "0000011100101000")
        self.m.set_word(7, "0101110100101000")
        self.m.set_word(8, "0001011000100000")
        self.m.set_word(9, "0100111100101000")
        self.m.set_word(10, "0100011100101000")
        self.m.set_word(11, "0001111100101000")
        self.m.set_word(12, "0100011100101000")
        self.m.set_word(13, "0001011100101000")
        self.m.set_word(14, "0000111100101000")
        self.m.set_word(15, "0100011100101000")

    def test_AB(self):
        self.m.sum_fields("010")
        word_result = self.m.get_word(0)
        self.assertEqual([0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0], word_result)


class Matrix3(unittest.TestCase):
    def setUp(self):
        self.m = Matrix()
        self.m.set_word(0, "0100011000101000")
        self.m.set_word(1, "0100000100101000")
        self.m.set_word(2, "0010000100101000")
        self.m.set_word(3, "0001011100101000")
        self.m.set_word(4, "0100011100101000")
        self.m.set_word(5, "0101011100101000")
        self.m.set_word(6, "0000011100101000")
        self.m.set_word(7, "0101110100101000")
        self.m.set_word(8, "0001011000100000")
        self.m.set_word(9, "0100111100101000")
        self.m.set_word(10, "0100011100101000")
        self.m.set_word(11, "0001111100101000")
        self.m.set_word(12, "0100011100101000")
        self.m.set_word(13, "0001011100101000")
        self.m.set_word(14, "0000111100101000")
        self.m.set_word(15, "0100011100101000")

    def test_con(self):
        self.m.conj(0, 1, 2)
        self.assertEqual(
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0], self.m.get_word(2)
        )
        self.assertEqual(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], self.m.get_diag(2)
        )

    def test_sheffer(self):
        self.m.sheffers_op(0, 1, 2)
        self.assertEqual(
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0], self.m.get_word(2)
        )
        self.assertEqual(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], self.m.get_diag(2)
        )

    def test_rep(self):
        self.m.rep_first(0, 1, 2)
        self.assertEqual(
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0], self.m.get_word(2)
        )
        self.assertEqual(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], self.m.get_diag(2)
        )

    def test_neg(self):
        self.m.neg_first(0, 1, 2)
        self.assertEqual(
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0], self.m.get_word(2)
        )
        self.assertEqual(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], self.m.get_diag(2)
        )

    def test_change_diag(self):
        self.m.set_diag(2, "1111111100000000")
        self.assertEqual(
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], self.m.get_diag(2)
        )


if __name__ == "__main__":
    unittest.main()
