def main():
    N, Q = map(int, input().split())
    A = list(range(N + 1))  # 1はじまりにするためにN+1の長さで作る、A[0]は使わない
    idx = list(range(N + 1))  # iの書かれたボールははじめi番目にある

    for _ in range(Q):
        x = int(input())
        fi = idx[x]  # xの位置
        si = fi + 1 if fi != N else fi - 1  # 通常は右隣のボールと入れ替えるが、右端なら左隣と入れ替える
        y = A[si]  # 入れ替えるボールに書かれた数
        A[fi], A[si] = A[si], A[fi]  # 入れ替える
        idx[x] = si  # xはsi、yはfiに移動
        idx[y] = fi
    print(*A[1:])  # A[0]を出力しないよう注意


if __name__ == '__main__':
    main()

"""
listってそう書けるんだ、知らなかった

indexメソッドにも、forと同じようにオーダーがかかる。
indexメソッドを使わずに解くことが今回の目的でもあったんだね。
ボールの場所を保存しておくようのlistを準備すればよかった。
覚えておこう
"""