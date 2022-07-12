l = [int(i) for i in list(input())]
number_l = [i for i in range(0,10)]
print(list(set(number_l)-set(l))[0])