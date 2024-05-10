class Variable:
    def __init__(self, positive: bool, char: str):
        self.positive: bool = positive
        self.char: str = char

    def __str__(self):
        return self.char if self.positive else "!" + self.char

    def copy(self):
        return Variable(self.positive, self.char)

    def __repr__(self):
        return self.char if self.positive else "!" + self.char

    def __eq__(self, other):
        return self.char == other.char and self.positive == other.positive


class Form:
    def __init__(self):
        self.expr_form = []

    def __str__(self):
        result = ""
        for elem in self.expr_form:
            result += str(elem) + " "
        return result

    def __getitem__(self, key):
        return self.expr_form[key]

    def __setitem__(self, key, value):
        self.expr_form[key] = value

    def append(self, var: Variable):
        self.expr_form.append(var)

    def length(self):
        return len(self.expr_form)

    def is_compatible(self, other):
        if self.length() != other.length():
            return False, None

        identic_counter, partially_identic_counter = 0, 0
        partially_char = None
        for elem in self.expr_form:
            for other_elem in other.expr_form:
                if elem.char == other_elem.char:
                    if elem.positive == other_elem.positive:
                        identic_counter += 1
                    else:
                        partially_identic_counter += 1
                        partially_char = elem.char
                    continue

        if partially_identic_counter != 1 or identic_counter != len(self.expr_form) - 1:
            return False, None

        new_form = Form()
        for elem in self.expr_form:
            if elem.char != partially_char:
                new_form.append(elem.copy())

        return True, new_form

    def is_other_included(self, other):
        for other_elem in other.expr_form:
            found = False
            for elem in self.expr_form:
                if (
                    other_elem.char == elem.char
                    and other_elem.positive == elem.positive
                ):
                    found = True
                    break

            if found is False:
                return False

        return True


def form_to_str(form, char):
    result = ""
    for elem in form:
        result += str(elem) + char
    result = result[:-1]
    return result


def full_form_to_str(full_form, char):
    result = ""
    if char == "|":
        char_in = "&"
    else:
        char_in = "|"

    for form in full_form:
        result += "("
        result += form_to_str(form, char_in)
        result += ")" + char

    result = result[:-1]
    return result

area_sizes = [
    [1, 8],
    [8, 1],
    [4, 4],
    [2, 4],
    [4, 2],
    [2, 2],
    [1, 4],
    [4, 1],
    [1, 2],
    [2, 1],
    [1, 1],
]
