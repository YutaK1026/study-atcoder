import sys
small_alpha = [chr(ord("a")+i) for i in range(26)]
large_alpha = [chr(ord("A")+i) for i in range(26)]
correct_s = 0
correct_l = 0
S = list(input())
for i in range(len(S)):
    if S[i] in small_alpha:
        small_alpha.remove(S[i])
        correct_s += 1
    elif S[i] in large_alpha:
        large_alpha.remove(S[i])
        correct_l += 1
    else:
        print("No")
        sys.exit()
if correct_s != 0 and correct_l != 0:
    print("Yes")
else:
    print("No")