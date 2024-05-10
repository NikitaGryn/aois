import itertools
import math


class TruthTable:

    def __init__(self, expression: str):
        self.operations = ["&", "!", "|", "-", "~", "(", ")"]
        variables = {}
        rpn: str = self._form_RPN(expression, variables)

        table = []
        l_values = [False, True]
        all_permutations = [
            list(i) for i in itertools.product(l_values, repeat=len(variables))
        ]
        for permutation in all_permutations:
            for ind, variable in enumerate(variables):
                variables[variable] = permutation[ind]

            table.append(permutation)
            table[-1].append(self._evaluate_RPN(rpn, variables))
        self.variables = list(variables.keys())
        self.table = table

    def get_variables(self):
        return self.variables

    def get_table(self):
        return self.table

    def print(self):
        for variable in self.variables:
            print("{:<3}".format(variable), end="")
        print("{:<3}".format("res"))
        for row in self.table:
            for elem in row:
                print("{:<3}".format("1" if elem else "0"), end="")
            print()

    def get_SDNF(self):
        result = ""
        for row in self.table:
            if row[-1] is True:
                result += "("
                for ind, elem in enumerate(row[:-1]):
                    result += "" if elem is True else "!"
                    result += f"{self.variables[ind]}&"
                result = result[:-1]
                result += ")|"

        return result[:-1]

    def get_SKNF(self):
        result = ""
        for row in self.table:
            if row[-1] is False:
                result += "("
                for ind, elem in enumerate(row[:-1]):
                    result += "" if elem is False else "!"
                    result += f"{self.variables[ind]}|"
                result = result[:-1]
                result += ")&"

        return result[:-1]

    def get_number_forms(self):
        conjuctions = []
        disjunctions = []
        for ind, row in enumerate(self.table):
            if row[-1]:
                disjunctions.append(str(ind))
            else:
                conjuctions.append(str(ind))

        conj_str = ", ".join(conjuctions)
        disj_str = ", ".join(disjunctions)
        return f"({conj_str}) /\\\n({disj_str}) \\/"

    def get_index_form(self):
        string = ""
        for row in self.table:
            string += "1" if row[-1] else "0"
        number = 0
        for ind, char in enumerate(reversed(string)):
            if char == "1":
                number += math.pow(2, ind)

        return number

    def _form_RPN(self, expression: str, variables) -> str:
        priority = {"!": 3, "&": 2, "|": 1, "-": 0, "~": 0, "(": -1, ")": 0}
        li = []
        result = ""
        for char in expression:
            if char == ">" or char == " ":
                continue

            if char in self.operations:
                if char == "(":
                    li.append(char)
                else:
                    while li and priority[li[-1]] >= priority[char]:
                        result += li.pop()

                    if char == ")":
                        li.pop()
                    else:
                        li.append(char)
            else:
                variables[char] = False
                result += char
        while li:
            char = li.pop()
            result += char
            if char not in self.operations:
                variables[char] = False
        return result

    def _apply_binary_operation(self, right, left, operation) -> bool:
        result = False
        if operation == "&":
            result = right & left
        elif operation == "|":
            result = right | left
        elif operation == "-":
            result = (not right) | left
        elif operation == "~":
            result = (right == left)
        return result

    def _stack_pop_to_bool(self, stack, variables) -> bool:
        element = stack.pop()
        if element is not False and element is not True:
            return variables[element]
        return element

    def _evaluate_RPN(self, rpn: str, variables) -> bool:
        stack = []
        for currentChar in rpn:
            if currentChar not in self.operations:
                stack.append(currentChar)

            else:
                if currentChar == "!":
                    var = stack.pop()
                    result = variables[var]
                    stack.append(not result)
                else:
                    left = self._stack_pop_to_bool(stack, variables)
                    right = self._stack_pop_to_bool(stack, variables)
                    stack.append(self._apply_binary_operation(right, left, currentChar))

        return stack.pop()
