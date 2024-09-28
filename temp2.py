table = [
    0,
    0,
    0,
    0,
    1,
    1,
    4,
    5,
    10,
    10,
    13,
    9,
    9,
    7,
    4,
    2,
    1,
    0,
    0,
    0,
    0,
]

table_2 = [
    0,
    0,
    0,
    0,
    1,
    1,
    2,
    4,
    4,
    4,
    3,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

new_table = table.copy()
print(sum(new_table))

for i in range(len(table) - 1):
    new_table[i + 1] += table[i] * 3

print(new_table)
print(sum(new_table))

for i in range(len(table) - 1):
    new_table[i + 1] += table_2[i]

print(new_table)
print(sum(new_table))
