from truth_table import TruthTable

if __name__ == "__main__":
    table = TruthTable("(a|b)&(!c)")
    table.print()
    print(table.get_SDNF())
    print(table.get_SKNF())
    print(table.get_index_form())
    print(table.get_number_forms())
