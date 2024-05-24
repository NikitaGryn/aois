from hash_table import HashTable

if __name__ == "__main__":
    t = HashTable()
    for i in range(20):
        t.add(str(i), i)
    print(t.get("19"))
