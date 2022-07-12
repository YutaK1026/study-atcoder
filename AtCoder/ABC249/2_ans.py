def judge():
    S = input()
    b1 = not S.islower()
    b2 = not S.isupper()
    b3 = len(S) == len(set(S))
    return b1 and b2 and b3


print("Yes" if judge() else "No")

"""
Sが全て小文字 : S.islower() = True
↓
Sに大文字が少なくとも一つ含まれる : not S.islower() = True
Sに小文字が少なくとも一つ含まれる : not S.isupper() = True

Sに出てくる文字の種類 : set(S)
これをつかえば一瞬で終わった。覚えておこうね

return の中身が全てTrueの時、print("Yes" if judge() else "No")のような記法が使える。内包表記だね。かっこいい、使いたいなぁ

個人的に、listの中から削除して、といった手法は、前にも出てきた手法だから、それを取ることが出来て少し嬉しい。
んでも、ちゃんとした関数使った方が早いし楽だから、覚えよう。
"""