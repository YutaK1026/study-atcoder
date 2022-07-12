N, K, X = map(int, input().split())

l = list(map(int, input().split()))
ans = 0
#i = 0
"""
for j in range(K):
    if l[i] - X >= 0:
        print("j+1して引いたよ")
        l[i] = l[i] - X
        print(l[i])
    if l[i] - X < 0:
        while l[i] - X < 0:
            print("")
            i += 1
        l[i] = l[i] - X
        print("i+1したよ そして引いたよ")
        print(l[i])
"""

for i in range(N):
    K_1 = int(l[i] / X)
    if K - K_1 >= 0:
        ans += l[i]%X
        K = K - K_1
    else:
        ans += l[i]-K*X

print(ans)



