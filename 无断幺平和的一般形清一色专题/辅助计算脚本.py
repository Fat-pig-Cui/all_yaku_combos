table = [
    0,  # 0
    0,  # 1
    0,  # 2
    0,  # 3
    0,  # 4
    0,  # 5
    1,  # 6
    1,  # 7
    2,  # 8
    2,  # 9
    3,  # 10
    0,  # 11
    2,  # 12
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
    0,  # 2
    0,  # 3
    0,  # 4
    0,  # 5
    1,  # 6
    1,  # 7
    2,  # 8
    1,  # 9
    2,  # 10
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
    0,  # 2
    0,  # 3
    0,  # 4
    0,  # 5
    1,  # 6
    1,  # 7
    2,  # 8
    2,  # 9
    2,  # 10
    0,  # 11
    1,  # 12
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
    0,  # 2
    0,  # 3
    0,  # 4
    0,  # 5
    1,  # 6
    1,  # 7
    2,  # 8
    2,  # 9
    2,  # 10
    0,  # 11
    1,  # 12
    0,  # 13
    0,  # 14
    0,  # 15
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
    0,  # 4
    0,  # 5
    1,  # 6
    1,  # 7
    2,  # 8
    2,  # 9
    1,  # 10
    0,  # 11
    1,  # 12
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
    {"fan": 1, "num": 1},
    {"fan": 2, "num": 2},
    {"fan": 3, "num": 2},
    {"fan": 4, "num": 1},
]

table_3_info = [
    {"fan": 1, "num": 1},
    {"fan": 2, "num": 2},
    {"fan": 3, "num": 3},
    {"fan": 4, "num": 2},
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
#
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
