def solve():
    A, B, K = map(int, input().split())
    curr = A  # スライムが今何匹か
    ans = 0  # すぬけくんが叫んだ回数
    while not (curr >= B):
        ans += 1  # すぬけくんが叫ぶと
        curr *= K  # スライムがK倍に増える
    return ans


print(solve())

"""
for while if文に、notを追加できるようにするといいね。
その方がスマートだしカッコいいし、そうでなければ面倒になる問題も今後増えてきそう。
*=なんてものもあるんだ、知らんかったわ
"""