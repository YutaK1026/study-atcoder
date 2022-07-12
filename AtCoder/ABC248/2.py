A, B, K = map(int, input().split())
n = 0
if (A>= B):
    print(n)
else:
    while True:
        n += 1
        A = A*K
        if A>= B:
            print(n)
            break