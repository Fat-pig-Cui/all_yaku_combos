table = [
    0,  # 0
    5,  # 1
    11,  # 2
    15,  # 3
    18,  # 4
    20,  # 5
    17,  # 6
    13,  # 7
    9,  # 8
    3,  # 9
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

table_2 = [
    0,  # 0
    5,  # 1
    11,  # 2
    14,  # 3
    17,  # 4
    20,  # 5
    16,  # 6
    12,  # 7
    9,  # 8
    3,  # 9
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
    {"fan": 1, "num": 2},
    {"fan": 2, "num": 3},
    {"fan": 3, "num": 2},
]

table_2_info = [
    {"fan": 1, "num": 2},
    {"fan": 2, "num": 4},
    {"fan": 3, "num": 5},
    {"fan": 4, "num": 4},
]

new_table = table.copy()
print(sum(new_table))

for info in table_info:
    for i in range(len(table) - info["fan"]):
        new_table[i + info["fan"]] += table[i] * info["num"]

for info in table_2_info:
    for i in range(len(table_2) - info["fan"]):
        new_table[i + info["fan"]] += table_2[i] * info["num"]


print(new_table)
print(sum(new_table))
