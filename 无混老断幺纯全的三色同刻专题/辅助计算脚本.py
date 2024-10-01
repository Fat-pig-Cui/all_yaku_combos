table = [
    0,  # 0
    0,  # 1
    1,  # 2
    0,  # 3
    2,  # 4
    0,  # 5
    3,  # 6
    5,  # 7
    3,  # 8
    5,  # 9
    1,  # 10
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
    0,  # 1
    1,  # 2
    0,  # 3
    1,  # 4
    0,  # 5
    2,  # 6
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

table_3 = [
    0,  # 0
    0,  # 1
    1,  # 2
    0,  # 3
    2,  # 4
    0,  # 5
    2,  # 6
    5,  # 7
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

table_4 = [
    0,  # 0
    0,  # 1
    1,  # 2
    0,  # 3
    1,  # 4
    0,  # 5
    1,  # 6
    0,  # 7
    0,  # 8
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

table_3_info = [
    {"fan": 3, "num": 1},
]

table_4_info = [
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


print(new_table)
print(sum(new_table))
