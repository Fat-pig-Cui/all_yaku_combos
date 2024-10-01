table = [
    0,  # 0
    0,  # 1
    0,  # 2
    1,  # 3
    0,  # 4
    1,  # 5
    1,  # 6
    0,  # 7
    1,  # 8
    0,  # 9
    0,  # 10
    0,  # 11
    0,  # 12
    0,  # 13
    0,  # 14
    0,  # 15
    0,  # 16
    0,  # 17
    0,  # 18
    0,  # 19
    0,  # 20
]

table_info = [
    {"fan": 1, "num": 3},
    {"fan": 2, "num": 5},
    {"fan": 3, "num": 5},
    {"fan": 4, "num": 3},
]

new_table = table.copy()
print(sum(new_table))

for info in table_info:
    for i in range(len(table) - info["fan"]):
        new_table[i + info["fan"]] += table[i] * info["num"]

print(new_table)
print(sum(new_table))
