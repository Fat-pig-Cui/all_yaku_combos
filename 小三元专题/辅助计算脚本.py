table = [
    0,  # 0
    0,  # 1
    0,  # 2
    0,  # 3
    1,  # 4
    0,  # 5
    2,  # 6
    1,  # 7
    6,  # 8
    3,  # 9
    8,  # 10
    5,  # 11
    7,  # 12
    6,  # 13
    6,  # 14
    4,  # 15
    2,  # 16
    1,  # 17
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
    0,  # 5
    2,  # 6
    1,  # 7
    2,  # 8
    2,  # 9
    3,  # 10
    3,  # 11
    4,  # 12
    3,  # 13
    2,  # 14
    1,  # 15
    0,  # 16
    0,  # 17
    0,  # 18
    0,  # 19
    0,  # 20
]

table_3 = [
    0,  # 0
    0,  # 1
    0,  # 2
    0,  # 3
    1,  # 4
    0,  # 5
    2,  # 6
    1,  # 7
    3,  # 8
    2,  # 9
    4,  # 10
    3,  # 11
    4,  # 12
    3,  # 13
    2,  # 14
    1,  # 15
    0,  # 16
    0,  # 17
    0,  # 18
    0,  # 19
    0,  # 20
]

table_4 = [
    0,  # 0
    0,  # 1
    0,  # 2
    0,  # 3
    1,  # 4
    0,  # 5
    2,  # 6
    1,  # 7
    5,  # 8
    3,  # 9
    6,  # 10
    4,  # 11
    4,  # 12
    3,  # 13
    2,  # 14
    1,  # 15
    0,  # 16
    0,  # 17
    0,  # 18
    0,  # 19
    0,  # 20
]

table_5 = [
    0,  # 0
    0,  # 1
    0,  # 2
    0,  # 3
    1,  # 4
    0,  # 5
    2,  # 6
    1,  # 7
    2,  # 8
    2,  # 9
    3,  # 10
    2,  # 11
    2,  # 12
    1,  # 13
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
    {"fan": 1, "num": 1},
    {"fan": 2, "num": 1},
    {"fan": 3, "num": 1},
]

table_3_info = [
    {"fan": 1, "num": 1},
    {"fan": 2, "num": 3},
    {"fan": 3, "num": 4},
    {"fan": 4, "num": 3},
]

table_4_info = [
    {"fan": 3, "num": 1},
]

table_5_info = [
    {"fan": 4, "num": 1},
]

new_table = table.copy()
print(sum(new_table))

for info in table_info:
    for i in range(len(table) - info["fan"]):
        new_table[i + info["fan"]] += table[i] * info["num"]

for info in table_2_info:
    for i in range(len(table_2) - info["fan"]):
        new_table[i + info["fan"]] += table_2[i] * info["num"]

for info in table_3_info:
    for i in range(len(table_3) - info["fan"]):
        new_table[i + info["fan"]] += table_3[i] * info["num"]

for info in table_4_info:
    for i in range(len(table_4) - info["fan"]):
        new_table[i + info["fan"]] += table_4[i] * info["num"]

for info in table_5_info:
    for i in range(len(table_5) - info["fan"]):
        new_table[i + info["fan"]] += table_5[i] * info["num"]

print(new_table)
print(sum(new_table))
