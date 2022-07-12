H, W = map(int, input().split())
R, C = map(int, input().split())
ans = 0
for r, c in ((R + 1, C), (R - 1, C), (R, C + 1), (R, C - 1)):
    if 1 <= r <= H and 1 <= c <= W:
        ans += 1
print(ans)

"""
ポイント
位置で判断できたね。
多角的に見る視点を育成しようね。

問題文をそのまま受け止めるのではなく、条件を自分で言い換える訓練が必要だね。
"""