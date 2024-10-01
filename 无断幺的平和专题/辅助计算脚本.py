table = [
    0,  # 0
    1,  # 1
    1,  # 2
    3,  # 3
    6,  # 4
    2,  # 5
    4,  # 6
    6,  # 7
    1,  # 8
    2,  # 9
    2,  # 10
    1,  # 11
    0,  # 12
    1,  # 13
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
    1,  # 1
    1,  # 2
    3,  # 3
    5,  # 4
    2,  # 5
    3,  # 6
    4,  # 7
    1,  # 8
    1,  # 9
    1,  # 10
    1,  # 11
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
    {"fan": 3, "num": 3},
]

table_2_info = [
    {"fan": 1, "num": 1},
    {"fan": 2, "num": 1},
    {"fan": 3, "num": 1},
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
