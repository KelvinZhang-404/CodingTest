l = ["A", "B", "A", "C", "D"]

s_r = [
    ["A", "B", "B", "C", "D"],
    ["C", "B", "A", "D", "B"],
    ["A", "B", "C", "D", "C"],
    ["B", "B", "A", "D", "A"],
    ["A", "B", "D", "D", "D"]
]

# x = {c: 0 for c in l}
# print(x)
x = [0 for _ in l]
s = len(s_r)
r = len(s_r[0])
for i in range(s):
    for j in range(r):
        if s_r[i][j] == l[j]:
            x[j] += 1

# print(s_r)
print(f"The easiest question is index {x.index(max(x))}")
