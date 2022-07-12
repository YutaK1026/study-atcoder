N, Q = map(int, input().split())
ans_list = []
for i in range(N):
    ans_list.append(i+1)
move_list=[]
for i in range(Q):
    move_list.append(input())
for i in range(Q):
    i = ans_list.index(int(move_list[i]))
    if i+1 == N:
        ans_list[i-1],ans_list[i] = ans_list[i],ans_list[i-1]
    else:
        ans_list[i],ans_list[i+1] = ans_list[i+1],ans_list[i]
ans_list = " ".join([str(_) for _ in ans_list])
print(ans_list)

"""
上の提出だと、やはり時間超過した。
時間がかかっているのは、明らかに順序変更の部分、現状オーダーが2*10^5で無理
オーダーを減らす必要がある。一般化出来ないかな？
今回は、数字に注目しているよね。listの順番じゃなくて。
現状は、数字をlistの順に直して処理したけれど、そうではなく、数字そのものを使う方法はないものか？
"""
