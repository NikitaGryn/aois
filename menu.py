from main import *


def main():
    number1 = int(input("Введите первое число: "))
    binary_number1 = number_to_binary(abs(number1))
    binary_number1 = binary_number1.zfill(7)

    direct_code_number1 = direct_code(number1, binary_number1)
    print("Прямой код для первого числа:", end=" ")
    for digit in direct_code_number1:
        print(digit, end=" ")
    print("\n", end="")

    inverse_code_number1 = inverse_code(direct_code_number1)
    print("Обратный код для первого числа:", end=" ")
    for digit in inverse_code_number1:
        print(digit, end=" ")
    print("\n", end="")

    additional_code_number1 = additional_code(number1, inverse_code_number1)
    print("Дополнительный код для первого числа:", end=" ")
    for digit in additional_code_number1:
        print(digit, end=" ")
    print("\n", end="")

    number2 = int(input("\nВведите второе число: "))
    binary_number2 = number_to_binary(abs(number2))
    binary_number2 = binary_number2.zfill(7)

    direct_code_number2 = direct_code(number2, binary_number2)
    print("\nПрямой код для второго числа:", end=" ")
    for digit in direct_code_number2:
        print(digit, end=" ")
    print("\n", end="")

    inverse_code_number2 = inverse_code(direct_code_number2)
    print("Обратный код для второго числа:", end=" ")
    for digit in inverse_code_number2:
        print(digit, end=" ")
    print("\n", end="")

    additional_code_number2 = additional_code(number2, inverse_code_number2)
    print("Дополнительный код для второго числа:", end=" ")
    for digit in additional_code_number2:
        print(digit, end=" ")
    print("\n", end="")
    print("\n", end="")

    sum_additional_code_number = additional_sum(additional_code_number1, additional_code_number2)
    print("Сумма в дополнительном коде:", ''.join(sum_additional_code_number), "число:", number1 + number2)

    difference_additional_code_number = additional_subtraction(number1, number2)
    print("Разность в дополнительном коде:", ''.join(difference_additional_code_number), "число:", number1 - number2)

    product, product_decimal = direct_multiplication(number1, number2)
    print("Произведение в прямом коде:", product, "число:", product_decimal)

    division = division_binary(number1, number2)
    print("Частное и остаток при делении:", division, 'число: ', number1/number2)

    number3 = float(input("Введите число с плавающей точкой: "))

    binary_representation1 = float_to_bin32(number3)
    print("Бинарное представление (IEEE-754-2008):", binary_representation1)

    number4 = float(input("Введите число с плавающей точкой: "))

    binary_representation2 = float_to_bin32(number4)
    print("Бинарное представление (IEEE-754-2008):", binary_representation2)

    summ_float = add_float32(number3, number4)
    print("Сумма:", summ_float, 'число:', number3 + number4)


if __name__ == "__main__":
    main()
