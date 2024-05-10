import unittest
from truth_table import TruthTable
from methods import get_SDNF_table, get_SKNF_table, get_SDNF_alg, get_SKNF_alg, get_SDNF_Karno, get_SKNF_Karno


class TestTruthTable1(unittest.TestCase):
    def setUp(self):
        self.table = TruthTable("(a&b)|!c")
        self.table.print()

    def test_SDNF(self):
        result = self.table.get_SDNF()
        expected = "(!a&!b&!c)|(!a&b&!c)|(a&!b&!c)|(a&b&!c)|(a&b&c)"
        self.assertEqual(expected, result)

    def test_SKNF(self):
        result = self.table.get_SKNF()
        expected = "(a|b|!c)&(a|!b|!c)&(!a|b|!c)"
        self.assertEqual(expected, result)

    def test_index_form(self):
        result = self.table.get_index_form()
        expected = 171.0
        self.assertEqual(expected, result)

    def test_number_forms(self):
        result = self.table.get_number_forms()
        expected = "(1, 3, 5) /\\\n(0, 2, 4, 6, 7) \\/"
        self.assertEqual(expected, result)


class TestTruthTable2(unittest.TestCase):
    def setUp(self):
        self.table = TruthTable("(a->b)|(a&b&c)")

    def test_SDNF(self):
        result = self.table.get_SDNF()
        expected = "(!a&!b&!c)|(!a&!b&c)|(!a&b&!c)|(!a&b&c)|(a&b&!c)|(a&b&c)"
        self.assertEqual(expected, result)

    def test_SKNF(self):
        result = self.table.get_SKNF()
        expected = "(!a|b|c)&(!a|b|!c)"
        self.assertEqual(expected, result)

    def test_index_form(self):
        result = self.table.get_index_form()
        expected = 243.0
        self.assertEqual(expected, result)

    def test_number_forms(self):
        result = self.table.get_number_forms()
        expected = "(4, 5) /\\\n(0, 1, 2, 3, 6, 7) \\/"
        self.assertEqual(expected, result)


class TestTruthTable3(unittest.TestCase):
    def setUp(self):
        self.table = TruthTable("(a&b)&!a&!c->d")

    def test_SDNF(self):
        result = self.table.get_SDNF()
        expected = "(!a&!b&!c&!d)|(!a&!b&!c&d)|(!a&!b&c&!d)|(!a&!b&c&d)|(!a&b&!c&!d)|(!a&b&!c&d)|(!a&b&c&!d)|(!a&b&c&d)|(a&!b&!c&!d)|(a&!b&!c&d)|(a&!b&c&!d)|(a&!b&c&d)|(a&b&!c&!d)|(a&b&!c&d)|(a&b&c&!d)|(a&b&c&d)"
        self.assertEqual(expected, result)

    def test_SKNF(self):
        result = self.table.get_SKNF()
        expected = ""
        self.assertEqual(expected, result)

    def test_index_form(self):
        result = self.table.get_index_form()
        expected = 65535.0
        self.assertEqual(expected, result)

    def test_number_forms(self):
        result = self.table.get_number_forms()
        expected = "() /\\\n(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) \\/"
        self.assertEqual(expected, result)


class TestAlgMethod(unittest.TestCase):
    def test_1_SDNF(self):
        result = get_SDNF_alg("(a&b)->c")
        expected = "(!a)|(!b)|(c)"
        self.assertEqual(expected, result)

    def test_2_SDNF(self):
        result = get_SDNF_alg("((a|b)&!c)&d->a")
        expected = "(!b)|(!d)|(c)|(a)"
        self.assertEqual(expected, result)

    def test_3_SDNF(self):
        result = get_SDNF_alg("(a&b&c|!a)")
        expected = "(b&c)|(!a)"
        self.assertEqual(expected, result)

    def test_1_SKNF(self):
        result = get_SKNF_alg("(a&b)->c")
        expected = "(!a|!b|c)"
        self.assertEqual(expected, result)

    def test_2_SKNF(self):
        result = get_SKNF_alg("((a|b)&!c)&d->a")
        expected = "(a|!b|c|!d)"
        self.assertEqual(expected, result)

    def test_3_SKNF(self):
        result = get_SKNF_alg("(a&b&c|!a)")
        expected = "(!a|b)&(!a|c)"
        self.assertEqual(expected, result)



class TestTableMethod(unittest.TestCase):
    def test_1_SDNF(self):
        result = get_SDNF_table("(a&b)->c")
        expected = "(!a)|(!b)|(c)"
        self.assertEqual(expected, result)

    def test_2_SDNF(self):
        result = get_SDNF_table("((a|b)&!c)&d->a")
        expected = "(!b)|(!d)|(c)|(a)"
        self.assertEqual(expected, result)

    def test_3_SDNF(self):
        result = get_SDNF_table("(a&b&c|!a)")
        expected = "(b&c)|(!a)"
        self.assertEqual(expected, result)

    def test_1_SKNF(self):
        result = get_SKNF_table("(a&b)->c")
        expected = "(!a|!b|c)"
        self.assertEqual(expected, result)

    def test_2_SKNF(self):
        result = get_SKNF_table("((a|b)&!c)&d->a")
        expected = "(a|!b|c|!d)"
        self.assertEqual(expected, result)

    def test_3_SKNF(self):
        result = get_SKNF_table("(a&b&c|!a)")
        expected = "(!a|b)&(!a|c)"
        self.assertEqual(expected, result)


class TestKarnoMap(unittest.TestCase):
    def test_1_SDNF(self):
        result = get_SDNF_Karno("(a&b)->c")
        expected = "(!b)|(c)|(!a)"
        self.assertEqual(expected, result)

    def test_2_SDNF(self):
        result = get_SDNF_Karno("((a|b)&!c)&d->a")
        expected = "(a)|(!b)|(c)|(!d)"
        self.assertEqual(expected, result)

    def test_3_SDNF(self):
        result = get_SDNF_Karno("(a&b&c|!a)")
        expected = "(!a)|(b&c)"
        self.assertEqual(expected, result)

    def test_1_SKNF(self):
        result = get_SKNF_Karno("(a&b)->c")
        expected = "(!a|!b|c)"
        self.assertEqual(expected, result)

    def test_2_SKNF(self):
        result = get_SKNF_Karno("((a|b)&!c)&d->a")
        expected = "(a|!b|c|!d)"
        self.assertEqual(expected, result)

    def test_3_SKNF(self):
        result = get_SKNF_Karno("(a&b&c|!a)")
        expected = "(!a|b)&(!a|c)"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
