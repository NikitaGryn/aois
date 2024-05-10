import methods

if __name__ == "__main__":
    print(f"result: {methods.get_SDNF_alg('(a&b&c|!a)')}")
    print(f"result: {methods.get_SKNF_alg('(a&b&c|!a)')}")
    print(f"result: {methods.get_SDNF_table('(a&b&c|!a)')}")
    print(f"result: {methods.get_SKNF_table('(a&b&c|!a)')}")
    print(f"result: {methods.get_SDNF_Karno('(a&b&c|!a)')}")
    print(f"result: {methods.get_SKNF_Karno('(a&b&c|!a)')}")
