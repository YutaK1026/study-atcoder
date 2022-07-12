"""import sys
N = int(input())
S = [list(map(str, input().split())) for _ in range(N)]
for i in range(len(S)):
    for j in range(len(S)):
        if (S[i][0] in S[j]) and (S[i][1] in S[j]):
            print("No")
            sys.exit()
print("Yes")
"""
import sys
import itertools
N = int(input())
S = list(itertools.chain.from_iterable([list(map(str, input().split())) for _ in range(N)]))
for i in range(0,len(S),2):
    if S.count(S[i]) >= 2 and S.count(S[i+1]) >= 2 and S[i] != S[i+1]:
        print("No")
        sys.exit()
print("Yes")
        