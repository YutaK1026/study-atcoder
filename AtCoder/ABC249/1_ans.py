def solve():
    def calc(p, q, r):
        """p秒間秒速qメートルで歩き、r秒間休むことを繰り返す人がx秒で進む距離を計算"""
        t = 0  # 経過時間
        dist = 0  # 進んだ距離
        while True:
            # p秒間歩く
            for _ in range(p):
                t += 1
                dist += q
                if t == x:  # x秒経過したら終了
                    return dist
            # r秒間休む
            for _ in range(r):
                t += 1
                if t == x:
                    return dist

    a, b, c, d, e, f, x = map(int, input().split())
    tak = calc(a, b, c)
    aok = calc(d, e, f)
    if tak == aok:
        return "Draw"
    if tak > aok:
        return "Takahashi"
    else:  # tak < aok
        return "Aoki"


print(solve())

"""
forつかわなくても、割れば良い
%で余りを求めれば、最後歩いているか否かの判別が出来る

このレベルでforにあまえているようでは、Oが非常に大きくなっていったときにTEAするよ

ちなみにミスを連発したのは、不等号の向きが違ったからです
ばーか

俺のコードは、可読性の低いコードになってるよね
出来る問題ほど、可読性を意識して書くようにしよう
"""