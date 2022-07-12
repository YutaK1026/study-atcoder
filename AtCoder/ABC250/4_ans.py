from collections import deque


def enum_primes(n):
    prime_flag = [1] * (n + 1)
    prime_flag[0] = 0
    prime_flag[1] = 0

    i = 2
    while i * i <= n:
        if prime_flag[i]:
            for j in range(2 * i, n + 1, i):
                prime_flag[j] = 0
        i += 1
    return [i for i in range(n + 1) if prime_flag[i]]


def main():
    N = int(input())
    ans = 0
    primes = enum_primes(10 ** 6 + 5)  # 素数が小さい順に入っています
    M = len(primes)

    for i in range(M):
        t = primes[i] ** 3  # 重い t = q ** 3を先に計算します
        for j in range(i):  # primes[i]未満の素数を小さい順に全探索
            if t * primes[j] > N:
                break
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()


"""
p*(q**3)なので、qのオーダーは多くても10**6であることがわかる
そして、その間の素数は数限られてくるので、今回は全探索でも間に合った。

今回のポイント
「あらかじめ素数のリストを作っておく」
N以下の自然数に対して行う、ってのはあほらしい
素数のリストを作っておいて、その中から任意の自然数を2個取り出して、かけあわせたものがN以下か否か、といったところに注目すればすぐに終わったね。。。
言われてみればマジで一瞬で理解できる分、解けなかったことが悔しい。せめてロジックくらい導きたかった

"""