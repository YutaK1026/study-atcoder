A = list(map(int, input().split()))
X = int(input())
Q = sum(x // X for x in A)
print(Q)
