N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(A)
rem = K  # クーポンの残り枚数
Q = sum(x // X for x in A)  # X円引きできる回数
"""
Qには整数値が入る。ただのint型だわな、そりゃそう
"""
R = sorted((x % X for x in A), reverse=True)  # X円引きし終わったあとの余りを大きい順に並べる
ans -= X * min(Q, rem)  # Qとクーポンの枚数の少ない方だけX円引きできる
rem -= min(Q, rem)  # X円引きに使った分クーポンを減らす
ans -= sum(R[:rem])  # 大きい順に使う（スライスは配列外参照を起こさないので、remが巨大でも問題ありません）
print(ans)

"""
x // xってなぁに？？？
⇒割り算の整数部だってさ、四則演算なのに知らんかったわ
https://note.nkmk.me/python-arithmetic-operator/

Qの処理頭良すぎない？？？え？？？
それぞれに適応出来るクーポンの枚数を合計して、それとクーポンの枚数を比較して、少ない方で引く、とか…
やば

その後は何をしている？
あーーー、50円のものに100円引きクーポン使って0円にする処理だ
その為に余りをソートしたのか、あったまいいねぇ～～！

ちなみに、この「引けるものをとりあえず全部引く」ってやつを

"""