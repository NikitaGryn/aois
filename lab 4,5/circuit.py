from KarnoMap import KarnoMap
from truth_table import TruthTable


def get_plus5():
    table_y0 = TruthTable("a&b&c&d").get_table()
    table_y1 = TruthTable("a&b&c&d").get_table()
    table_y2 = TruthTable("a&b&c&d").get_table()
    table_y3 = TruthTable("a&b&c&d").get_table()
    solution_y0 = [False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, False]
    solution_y1 = [True, True, True, False, False, False, False, True, True, True, False, False, False, False, False, False]
    solution_y2 = [False, True, True, False, False, True, True, False, False, True, False, False, False, False, False, False]
    solution_y3 = [True, False, True, False, True, False, True, False, True, False, False, False, False, False, False, False]
    for i in range(len(table_y0)):
        table_y0[i][-1] = solution_y0[i]
        table_y1[i][-1] = solution_y1[i]
        table_y2[i][-1] = solution_y2[i]
        table_y3[i][-1] = solution_y3[i]
    truth_y0 = TruthTable("a&b&c&d")
    truth_y0.set_table(table_y0)
    truth_y1 = TruthTable("a&b&c&d")
    truth_y1.set_table(table_y1)
    truth_y2 = TruthTable("a&b&c&d")
    truth_y2.set_table(table_y2)
    truth_y3 = TruthTable("a&b&c&d")
    truth_y3.set_table(table_y3)
    sknf_y0 = truth_y0.get_SDNF()
    sknf_y1 = truth_y1.get_SDNF()
    sknf_y2 = truth_y2.get_SDNF()
    sknf_y3 = truth_y3.get_SDNF()
    min_y0 = KarnoMap(table_y0, ["a", "b", "c", "d"]).get_SDNF()
    min_y1 = KarnoMap(table_y1, ["a", "b", "c", "d"]).get_SDNF()
    min_y2 = KarnoMap(table_y2, ["a", "b", "c", "d"]).get_SDNF()
    min_y3 = KarnoMap(table_y3, ["a", "b", "c", "d"]).get_SDNF()
    print(f'y0: {sknf_y0}\ny1: {sknf_y1}\ny2: {sknf_y2}\ny3: {sknf_y3}')
    print(f'min y0: {min_y0}\nmin y1: {min_y1}\nmin y2: {min_y2}\nmin y3: {min_y3}')
    print()
    print('-------------------')
    print()


def get_sum():
    table_S = TruthTable("a&b&c").get_table()
    table_P = TruthTable("a&b&c").get_table()
    solution_S = [False, True, True, False, True, False, False, True]
    solution_P = [False, True, True, True, False, False, False, True]
    for i in range(len(table_S)):
        table_S[i][-1] = solution_S[i]
        table_P[i][-1] = solution_P[i]

    truth_S = TruthTable("a&b&c")
    truth_S.set_table(table_S)
    truth_P = TruthTable("a&b&c")
    truth_P.set_table(table_P)
    sknf_S = truth_S.get_SDNF()
    sknf_P = truth_P.get_SDNF()

    min_S = KarnoMap(table_S, ["a", "b", "c"]).get_SDNF()
    min_P = KarnoMap(table_P, ["a", "b", "c"]).get_SDNF()
    print(f'y0: {sknf_S}\ny1: {sknf_P}')
    print(f'min y0: {min_S}\nmin y1: {min_P}')
    print()
    print('-------------------')
    print()


def get_triggers():
    table_h1 = TruthTable("a&b&c&d").get_table()
    table_h2 = TruthTable("a&b&c&d").get_table()
    table_h3 = TruthTable("a&b&c&d").get_table()
    solution_h1 = [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]
    solution_h2 = [False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False]
    solution_h3 = [False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False]
    for i in range(len(table_h1)):
        table_h1[i][-1] = solution_h1[i]
        table_h2[i][-1] = solution_h2[i]
        table_h3[i][-1] = solution_h3[i]

    truth_y0 = TruthTable("a&b&c&d")
    truth_y0.set_table(table_h1)
    truth_y1 = TruthTable("a&b&c&d")
    truth_y1.set_table(table_h2)
    truth_y2 = TruthTable("a&b&c&d")
    truth_y2.set_table(table_h3)
    sknf_h1 = truth_y0.get_SDNF()
    sknf_h2 = truth_y1.get_SDNF()
    sknf_h3 = truth_y2.get_SDNF()
    min_h1 = KarnoMap(table_h1, ["a", "b", "c", "d"]).get_SDNF()
    min_h2 = KarnoMap(table_h2, ["a", "b", "c", "d"]).get_SDNF()
    min_h3 = KarnoMap(table_h3, ["a", "b", "c", "d"]).get_SDNF()
    print(f'h1: {sknf_h1}\nh2: {sknf_h2}\nh3: {sknf_h3}')
    print(f'min h1: {min_h1}\nmin h2: {min_h2}\nmin h3: {min_h3}')
    print()
    print('-------------------')
    print()


