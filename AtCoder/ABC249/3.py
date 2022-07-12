"""
ノート忘れたから、ここに思考書いていこうかな？
N<15か、だったら全探索で何も問題ないね。
ゆーて15C7くらいが最大でしょ？いけるいける

import itertools

lis = [1,2,3,4]
for team in itertools.combinations(lis, 3):
	print(team)

という感じで組み合わせをタプル化して、それぞれに対応する文字列をzipして、setして、最大数を更新していく方針でいいんじゃない？
"""

import itertools
ans = 0
N, K = map(int, input().split())
l = [str(input()) for i in range(N)]
for i in range(1,N):
    for team in itertools.combinations(l, i):
        
        print(team)
        l_list = ''.join(team)
        if ans <= len(set(l_list)):
            ans = len(set(l_list))