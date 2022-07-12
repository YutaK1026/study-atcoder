from subprocess import list2cmdline


N = int(input())
list_a = [[1]]
for i in range(N):
    new_list_a = list_a[i] + [i+2] + list(reversed(list_a[i]))
    list_a.append(new_list_a)
list_a[N-1] = " ".join([str(_) for _ in list_a[N-1]])
print(list_a[N-1])