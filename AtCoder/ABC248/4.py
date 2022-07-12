N = int(input())
A = list(map(int, input().split()))
A_dict = {}

for i in range(len(A)):
    A_dict.setdefault(i+1,A[i])
A_list = list(A_dict.items())

Q = int(input())
S = [list(map(int, input().split())) for _ in range(Q)]
for i in range(Q):
    new_A_list =[]
    new_A_list = A_list[(S[i][0]-1):S[i][1]]
    ans = 0
    for j in range(len(new_A_list)):
        if new_A_list[j][1] ==S[i][2]:
            ans += 1
    print(ans)