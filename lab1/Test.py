import unittest
from main import *


class TestFunctions(unittest.TestCase):
    def test_code(self):
        binary_without_direct = number_to_binary(5)
        direct_code_number = direct_code(5, binary_without_direct)
        self.assertEqual(direct_code_number, '00000101')

        inverse_code_number = inverse_code(direct_code_number)
        self.assertEqual(inverse_code_number, '00000101')

        additional_code_number = additional_code(5, inverse_code_number)
        self.assertEqual(additional_code_number, '00000101')

        binary_without_direct2 = number_to_binary(5)
        direct_code_number2 = direct_code(-5, binary_without_direct2)
        self.assertEqual(direct_code_number2, '10000101')

        inverse_code_number2 = inverse_code(direct_code_number2)
        self.assertEqual(inverse_code_number2, '11111010')

        additional_code_number2 = additional_code(-5, inverse_code_number2)
        self.assertEqual(additional_code_number2, '11111011')

    def test_binary_to_number(self):
        result = binary_to_number('00000101')
        self.assertEqual(result, 5)

        result2 = binary_to_number('00000110')
        self.assertEqual(result2, 6)

    def test_sum(self):
        sum_additional_number = additional_sum('00000101', '00000011')
        self.assertEqual(''.join(sum_additional_number), '00001000')

    def test_difference(self):
        difference_additional_number = additional_subtraction(8, 3)
        self.assertEqual(''.join(difference_additional_number), '00000101')

    def test_multiplication(self):
        multiplication_number, product_decimal = direct_multiplication(2, -4)
        self.assertEqual(multiplication_number, '10001000')
        self.assertEqual(product_decimal, -8)

    def test_division(self):
        division_number = division_binary(6, 3)
        self.assertEqual('Quotient: 00000010, Remainder: 0000000', division_number)

    def test_float_number(self):
        float_number = float_to_bin32(23.5)
        self.assertEqual(float_number, '01000001101111000000000000000000')

    def test_sum_float_number(self):
        summ_float = sum_float(7.125, 18.5)
        self.assertEqual(summ_float, '01000001110011010000000000000000')


if __name__ == '__main__':
    unittest.main()
