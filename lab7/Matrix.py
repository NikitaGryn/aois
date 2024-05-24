class Element:
    def __init__(self, value: bool):
        self.value = value

    def get(self) -> bool:
        return self.value

    def __repr__(self):
        return "0" if self.value is False else "1"

    def __eq__(self, other):
        return self.value == other

    def __str__(self):
        return "0" if self.value is False else "1"

    def __int__(self):
        return 1 if self.value else 0


class Matrix:
    def __init__(self):
        self.__table = [[Element(False)] * 16 for i in range(16)]

    def get_word(self, ind):
        a = []
        for i in range(len(self.__table[ind])):
            a.append(self.get_elem(ind, i))

        return a

    def get_diag(self, ind):
        if ind > 16 or ind < 0:
            raise Exception("The index is out of bounds")

        a = []
        for i in range(len(self.__table)):
            a.append(self.get_elem(i, ind))
        return a

    def get_elem(self, collumn, row):
        return self.__table[collumn][(row + collumn) % 16]

    def set_elem(self, collumn: int, row: int, new_value: bool):
        self.__table[collumn][(row + collumn) % 16] = Element(new_value)

    def set_word(self, collumn: int, word: str):
        if len(word) != 16:
            raise Exception("The word has to be of lenght 16")

        for ind, char in enumerate(word):
            if char == "1":
                self.set_elem(collumn, ind, True)
            else:
                self.set_elem(collumn, ind, False)

    def set_diag(self, row: int, diag: str):
        if len(diag) != 16:
            raise Exception("The diagonal has to be of length 16")

        for ind, char in enumerate(diag):
            if char == "1":
                self.set_elem(ind, row, True)
            else:
                self.set_elem(ind, row, False)

    def conj(self, first_ind, second_ind, result_ind):
        for i in range(16):
            first_element = self.get_elem(i, first_ind)
            second_element = self.get_elem(i, second_ind)
            self.set_elem(i, result_ind, first_element.get() and second_element.get())

    def rep_first(self, first_ind, second_ind, result_ind):
        for i in range(16):
            first_element = self.get_elem(i, first_ind)
            self.set_elem(i, result_ind, first_element.get())

    def neg_first(self, first_ind, second_ind, result_ind):
        for i in range(16):
            first_element = self.get_elem(i, first_ind)
            self.set_elem(i, result_ind, not first_element.get())

    def sheffers_op(self, first_ind, second_ind, result_ind):
        for i in range(16):
            first_element = self.get_elem(i, first_ind)
            second_element = self.get_elem(i, second_ind)
            self.set_elem(
                i, result_ind, not (first_element.get() and second_element.get())
            )

    def sum_fields(self, key_value):
        if len(key_value) != 3:
            raise Exception("not valid lenght of the argument!")

        for i in range(len(self.__table)):
            if all(
                elem == str(self.get_elem(i, j)) for j, elem in enumerate(key_value)
            ):
                self.perform_sum_fields(i)

    def perform_sum_fields(self, collumn_ind):
        carry: int = 0
        for i in range(3, -1, -1):
            carry, new_value = divmod(
                int(self.get_elem(collumn_ind, i + 3))
                + int(self.get_elem(collumn_ind, i + 7))
                + int(carry),
                2,
            )
            new_value = False if new_value == 0 else True
            self.set_elem(collumn_ind, i + 12, new_value)
        new_value = False if carry == 0 else True

        self.set_elem(collumn_ind, 11, new_value)

    def print(self):
        for i in range(len(self.__table)):
            for j in range(len(self.__table[i])):
                print(f"{self.__table[j][i]} ", end="")
            print()

    def nearest_min(self, condition: str):
        if len(condition) != 16:
            raise Exception("the condition is not of size 16")

        above_elems = []
        for j in range(16):
            g_prev, g_value, l_prev, l_value = False, False, False, False
            for i in range(15, -1, -1):
                value: bool = True if condition[15 - i] == "1" else False
                s_value: bool = self.get_elem(j, 15 - i).get()
                g_value: bool = g_prev or (not value and s_value and not l_prev)
                l_value: bool = l_prev or (value and not s_value and not g_prev)
                g_prev = g_value
                l_prev = l_value

            if not g_value and l_value:
                above_elems.append(j)
        if len(above_elems) == 0:
            return None

        max_ind = 0
        for j in range(1, len(above_elems)):
            g_prev, g_value, l_prev, l_value = False, False, False, False
            for i in range(15, -1, -1):
                value: bool = self.get_elem(max_ind, 15 - i).get()
                S_value = self.get_elem(above_elems[j], 15 - i).get()
                g_value = g_prev or (not value and S_value and not l_prev)
                l_value = l_prev or (value and not S_value and not g_prev)
                g_prev = g_value
                l_prev = l_value
            if g_value and not l_value:
                max_ind = j

        return above_elems[max_ind]

    def nearest_max(self, condition: str):
        if len(condition) != 16:
            raise Exception("the condition is not of size 16")

        above_elems = []
        for j in range(16):
            g_prev, g_value, l_prev, l_value = False, False, False, False
            for i in range(15, -1, -1):
                value: bool = True if condition[15 - i] == "1" else False
                s_value: bool = self.get_elem(j, 15 - i).get()
                g_value: bool = g_prev or (not value and s_value and not l_prev)
                l_value: bool = l_prev or (value and not s_value and not g_prev)
                g_prev = g_value
                l_prev = l_value

            if g_value and not l_value:
                above_elems.append(j)

        if len(above_elems) == 0:
            return None

        min_ind = 0
        for j in range(1, len(above_elems)):
            g_prev, g_value, l_prev, l_value = False, False, False, False
            for i in range(15, -1, -1):
                value: bool = self.get_elem(min_ind, 15 - i).get()
                S_value = self.get_elem(above_elems[j], 15 - i).get()
                g_value = g_prev or (not value and S_value and not l_prev)
                l_value = l_prev or (value and not S_value and not g_prev)
                g_prev = g_value
                l_prev = l_value
            if not g_value and l_value:
                min_ind = j

        return above_elems[min_ind]
