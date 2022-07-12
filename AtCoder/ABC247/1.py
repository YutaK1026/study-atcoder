N = list(input())
ans = []
ans.append(0)
for i in range(3):
    if int(N[i]) == 0:
        ans.append(0)
    if int(N[i]) == 1:
        ans.append(1)
ans = "".join([str(_) for _ in ans])
print(ans)