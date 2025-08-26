import sys

sys.stdin = open('1970_easy_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = input()
    N = int(N)
    # print(N)

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * len(money)

    for i in range(len(money)):
        if N >= money[i]:
            while N >= money[i]:
                N = N - money[i]
                change[i] += 1
                # print(N)

    print(f'#{tc}')
    print(' '.join(map(str, change)))