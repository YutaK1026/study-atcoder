def solve():
    S = input()
    for i in range(10):
        if str(i) not in S:
            return i


print(solve())

"""
if文の、not、っていうのを使いこなせたらめちゃ便利だね…
存在しないものを求めたい時⇒notを使う、って体系化できたら強いかも
"""