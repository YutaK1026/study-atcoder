from bisect import bisect_left, bisect_right


def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    pos = [[] for _ in range(N + 1)]
    for i, x in enumerate(A, 1):
        pos[x].append(i)
    #print(pos)
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        B = pos[X]
        print(bisect_right(B, R) - bisect_left(B, L))


if __name__ == '__main__':
    main()

"""
新しいモジュールが出てきたね。bisectってやつ
2分探索をするためのもので、非常に高速で便利なやつらしい、すご

enumerateとは？
    関数の引数にリストなどのイテラブルオブジェクトを指定する。
    インデックス番号, 要素の順に取得できる。
例）
for i, name in enumerate(l):
    print(i, name)
# 0 Alice
# 1 Bob
# 2 Charlie
はああああああ～～～、なるほどねぇぇぇぇ

"""