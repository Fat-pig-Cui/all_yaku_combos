table = [
    0,  # 0
    0,  # 1
    0,  # 2
    0,  # 3
    1,  # 4
    5,  # 5
    11,  # 6
    15,  # 7
    18,  # 8
    20,  # 9
    17,  # 10
    13,  # 11
    9,  # 12
    3,  # 13
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
    0,  # 1
    0,  # 2
    0,  # 3
    1,  # 4
    5,  # 5
    10,  # 6
    10,  # 7
    8,  # 8
    10,  # 9
    9,  # 10
    3,  # 11
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
    {"fan": 3, "num": 1},
]

table_2_info = [
    {"fan": 1, "num": 2},
    {"fan": 2, "num": 4},
    {"fan": 3, "num": 5},
    {"fan": 4, "num": 3},
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
