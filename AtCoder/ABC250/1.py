H, W = map(int, input().split())
R, C = map(int, input().split())
ans = 0

if(H == 1 and W == 1):
    ans = 0
elif((H == 1 and (C == 1 or C == W))or(W == 1 and (R == 1 or R == H))):
    ans = 1
elif(H == 1 or W == 1):
    ans = 2
elif(H == 2 and W == 2):
    ans = 2
elif((R == 1 or R == H) and (C == W or C == 1)):
    ans = 2
elif((R == 1 or R == H) or (C == W or C == 1)):
    ans = 3
else:
    ans = 4
print(ans)
