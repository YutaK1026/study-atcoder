import sympy
N = int(input())
ans = 0
for i in range(N):
    if(len(sympy.factorint(N)) == 2):
        #if(sympy.factorint(N).values()[0] == 1 and sympy.factorint(N).values()[1] == 2):
        ans = ans + 1
print(type(sympy.facorint(N)))
print(ans)

"""
解けませんでした
"""