l = list(map(int, input().split()))
T_sec = l[6]
T_ans = 0
T = 0
A_sec = l[6]
A_ans = 0
A = 0
while(True):
    if T_sec - (l[0] + l[2]) > 0:
        T_ans += 1
        T_sec = T_sec - (l[0] + l[2]) 
    else:
        break
while(True):
    if A_sec - (l[3] + l[5]) > 0:
        A_ans += 1
        A_sec = A_sec - (l[3] + l[5])
    else:
        break
T = T_ans * l[1] * l[0]
A = A_ans * l[4] * l[3]

if T_sec > l[0]:
    T = T +l[1]*l[0]
else:
    T = T +T_sec*l[1]

if A_sec > l[3]:
    A = A + l[4]*l[3]
else:
    A = A + A_sec*l[4]


if (T > A):
    print("Takahashi")
elif (A > T):
    print("Aoki")
elif(A == T):
    print("Draw")