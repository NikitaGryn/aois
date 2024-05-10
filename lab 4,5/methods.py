from truth_table import TruthTable
from KarnoMap import KarnoMap
import re
from variable import *

def get_SDNF_alg(expr_str: str):
    table = TruthTable(expr_str)
    table.print()
    full_form = _get_form(table.get_SDNF())

    print(full_form_to_str(full_form, "|"))
    full_form = reduce_form(full_form)
    print(full_form_to_str(full_form, "|"))
    full_form = reduce_form_alg(full_form, True)

    return full_form_to_str(full_form, "|")


def get_SKNF_alg(expr_str: str):
    table = TruthTable(expr_str)
    table.print()
    full_form = _get_form(table.get_SKNF())

    print(full_form_to_str(full_form, "&"))
    print('ok')
    full_form = reduce_form(full_form)
    print(full_form_to_str(full_form, "&"))
    full_form = reduce_form_alg(full_form, False)
    return full_form_to_str(full_form, "&")


def get_SDNF_table(expr_str: str):
    table = TruthTable(expr_str)
    full_form = _get_form(table.get_SDNF())

    print(full_form_to_str(full_form, "|"))
    reduced_form = reduce_form(full_form)

    print("Before: ")
    print_table_minimization(full_form, reduced_form, "|")
    reduced_form = reduce_form_table(full_form, reduced_form, "|")
    print("After: ")
    print_table_minimization(full_form, reduced_form, "|")

    return full_form_to_str(reduced_form, "|")


def get_SKNF_table(expr_str: str):
    table = TruthTable(expr_str)
    full_form = _get_form(table.get_SKNF())

    print(full_form_to_str(full_form, "&"))
    reduced_form = reduce_form(full_form)

    print("Before: ")
    print_table_minimization(full_form, reduced_form, "&")
    reduced_form = reduce_form_table(full_form, reduced_form, "&")
    print("After: ")
    print_table_minimization(full_form, reduced_form, "&")

    return full_form_to_str(reduced_form, "&")


def get_SDNF_Karno(expr_str: str):
    table = TruthTable(expr_str)
    map = KarnoMap(table.get_table(), table.get_variables())
    return map.get_SDNF()

def get_SKNF_Karno(expr_str: str):
    table = TruthTable(expr_str)
    map = KarnoMap(table.get_table(), table.get_variables())
    return map.get_SKNF()

def print_table_minimization(full_form, reduced_form, char):
    char_in = "&" if char == "|" else "|"
    print(f"{'':<10}", end="")
    for form in full_form:
        print(f"{form_to_str(form, char_in):<10}", end="")
    print()
    for form in reduced_form:
        print(f"{form_to_str(form, char_in):<10}", end="")
        for form_full in full_form:
            print(f"{'x' if form_full.is_other_included(form) else ' ' :<10}", end="")

        print()


def reduce_form_table(full_form, reduced_form, char):
    table = []
    for reduced_elem in reduced_form:
        row = [full_elem.is_other_included(reduced_elem) for full_elem in full_form]
        table.append(row)

    i = 0
    while i < len(table):
        if all(
            any(table[k][j] for k in range(len(table)) if i != k)
            for j in range(len(table[i]))
        ):
            table.pop(i)
            reduced_form.pop(i)
            i -= 1
        i += 1
    return reduced_form


def reduce_form_alg(full_form, equal_cond):
    reduced = False
    while not reduced:
        reduced = True
        ind = 0
        while ind < len(full_form):
            if is_redundant_part(full_form, ind, equal_cond):
                full_form.pop(ind)
                ind -= 1
                reduced = False
            ind += 1
    return full_form


def is_redundant_part(full_form, ind, equal_cond):
    part = full_form[ind]
    solution = {}
    for elem in part:
        if elem.positive == equal_cond:
            solution[elem.char] = True
        else:
            solution[elem.char] = False

    for i in range(len(full_form)):
        if i == ind:
            continue

        for elem in full_form[i]:
            if solution.get(elem.char) is None:
                continue

            cond = not (solution[elem.char] != elem.positive)
            if cond:
                if cond == equal_cond:
                    return True
            else:
                if cond != equal_cond:
                    return True

    return False


def reduce_form(full_form):
    reduced = True
    while reduced:
        reduced = False
        to_delete = []
        new_forms = []
        for i in range(len(full_form)):
            for j in range(i + 1, len(full_form)):
                is_reduced, new_form = full_form[i].is_compatible(full_form[j])
                if is_reduced:
                    new_forms.append(new_form)
                    to_delete += [i, j]
                    reduced = True

        to_delete = set(to_delete)
        full_form = [el for ind, el in enumerate(full_form) if ind not in to_delete]
        full_form += new_forms

    return full_form


def _get_form(shortened_form: str):
    result = []
    in_brackets = re.findall(r"\((.*?)\)", shortened_form)
    for bracket in in_brackets:
        positive = True
        form_bracket = Form()
        for char in bracket:
            if char == "!":
                positive = False
                continue

            if char == "&" or char == "|":
                continue

            form_bracket.append(Variable(positive, char))
            positive = True

        result.append(form_bracket)

    return result
