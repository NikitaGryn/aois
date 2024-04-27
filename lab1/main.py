def number_to_binary(num):
    binary = ""
    for _ in range(7):
        binary = str(num % 2) + binary
        num //= 2
    return binary


def binary_to_number(binary_str):
    number = 0
    power = len(binary_str) - 1
    for bit in binary_str:
        if bit == '1':
            number += 2 ** power
        power -= 1
    return number


def direct_code(number, binary_number):
    if number < 0:
        return '1' + binary_number
    else:
        return '0' + binary_number


def inverse_code(direct):
    direct_list = list(direct)
    if direct_list[0] == '1':
        for i in range(1, 8):
            if direct_list[i] == '0':
                direct_list[i] = '1'
            else:
                direct_list[i] = '0'
    return ''.join(direct_list)


def additional_code(number, inverse):
    if number < 0:
        complement = list(inverse)
        carry = 1
        for i in range(7, -1, -1):
            if carry == 0:
                break
            if complement[i] == '0':
                complement[i] = '1'
                carry = 0
            else:
                complement[i] = '0'
        return ''.join(complement)
    else:
        return inverse


def additional_sum(additional1, additional2):
    sum_result = direct_sum(additional1, additional2)
    if sum_result[0] == '1':
        sum_result = inverse_code(sum_result)
        sum_result = additional_code(-1, sum_result)
    return sum_result


def direct_sum(direct1, direct2):
    sum_result = ['0'] * 8
    carry = 0
    for i in range(7, -1, -1):
        total = int(direct1[i]) + int(direct2[i]) + carry
        sum_result[i] = str(total % 2)
        carry = total // 2
    return sum_result


def additional_subtraction(number1, number2):
    additional_code_number2 = additional_code(-number2, inverse_code(
        direct_code(-number2, number_to_binary(abs(-number2)).zfill(7))))

    additional_code_number1 = additional_code(number1, inverse_code(
        direct_code(number1, number_to_binary(abs(number1)).zfill(7))))

    subtraction_result = additional_sum(additional_code_number1, additional_code_number2)

    return subtraction_result


def direct_multiplication(number1, number2):
    binary_number1 = number_to_binary(abs(number1)).zfill(7)
    binary_number2 = number_to_binary(abs(number2)).zfill(7)

    sign = '0' if (number1 >= 0 and number2 >= 0) or (number1 < 0 and number2 < 0) else '1'

    result = ['0'] * 14
    carry = 0
    for i in range(6, -1, -1):
        for j in range(6, -1, -1):
            total = int(result[i + j + 1]) + int(binary_number1[i]) * int(binary_number2[j]) + carry
            result[i + j + 1] = str(total % 2)
            carry = total // 2
        result[i] = str(carry)
        carry = 0

    product = ''.join(result)
    product = sign + product[7:]

    product_decimal = number1 * number2

    return product, product_decimal


def division_binary(num_1, num_2):
    if num_2 == 0:
        raise ValueError("Делитель не может быть равен нулю")

    sign = '1' if num_1 * num_2 < 0 else '0'

    dividend_binary = number_to_binary(abs(num_1))
    divisor_binary = number_to_binary(abs(num_2))

    dividend_len = len(dividend_binary)
    divisor_len = len(divisor_binary)

    quotient = 0
    remainder = 0

    for _ in range(dividend_len):
        remainder <<= 1
        remainder |= int(dividend_binary[_])
        if remainder >= binary_to_number(divisor_binary):
            remainder -= binary_to_number(divisor_binary)
            quotient = (quotient << 1) | 1
        else:
            quotient <<= 1

    quotient_str = ''
    for i in range(dividend_len):
        quotient_str += str((quotient >> (dividend_len - i - 1)) & 1)

    remainder_str = ''
    for i in range(divisor_len):
        remainder_str += str((remainder >> (divisor_len - i - 1)) & 1)

    result_str = "Quotient: " + sign + quotient_str + ", Remainder: " + remainder_str

    return result_str


def float_to_bin32(num):
    if num == 0:
        return '0' * 32

    sign_bit = '0'
    if num < 0:
        sign_bit = '1'
        num = -num

    exponent = 127

    while num >= 2:
        exponent += 1
        num /= 2
    while num < 1:
        exponent -= 1
        num *= 2

    fraction_int = int((num - 1) * (1 << 23))
    fraction_bits = ""
    for _ in range(23):
        fraction_bits = str(fraction_int % 2) + fraction_bits
        fraction_int //= 2

    exponent_bits = ""
    for _ in range(8):
        exponent_bits = str(exponent % 2) + exponent_bits
        exponent //= 2

    return sign_bit + exponent_bits + fraction_bits


def sum_float(num1, num2):
    num1 = float_to_bin32(num1)
    num2 = float_to_bin32(num2)

    exponent_number1 = binary_to_number(num1[1:9])
    exponent_number2 = binary_to_number(num2[1:9])
    mantissa_number1 = "1" + num1[9:]
    mantissa_number2 = "1" + num2[9:]

    while exponent_number1 < exponent_number2:
        mantissa_number1 = "0" + mantissa_number1[:-1]
        exponent_number1 += 1
    while exponent_number2 < exponent_number1:
        mantissa_number2 = "0" + mantissa_number2[:-1]
        exponent_number2 += 1

    carry = 0
    sum_mantiss = ""
    for i in range(23, -1, -1):
        bit1 = int(mantissa_number1[i])
        bit2 = int(mantissa_number2[i])
        total = bit1 + bit2 + carry
        sum_mantiss = str(total % 2) + sum_mantiss
        carry = total // 2

    if carry:
        sum_mantiss = "1" + sum_mantiss[:-1]
        exponent_number1 += 1

    exponent = ""
    for _ in range(8):
        exponent = str(exponent_number1 % 2) + exponent
        exponent_number1 //= 2

    exponent = exponent.rjust(8, '0')

    result_sum = num1[0] + exponent + sum_mantiss[1:]

    return result_sum
