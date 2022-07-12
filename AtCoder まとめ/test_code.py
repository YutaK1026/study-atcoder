A = [["aa"],["bb"],["cc"]]
pos = [[] for _ in range(3)]
for i, x in enumerate(A, 1):
        pos[x].append(i)
print(pos)