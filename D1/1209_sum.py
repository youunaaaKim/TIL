import sys
sys.stdin = open('1209_input.txt')

T = 10
for _ in range(T):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    #print(arr)

    results = []


    # 행 합
    for i in range(100):
        ans = sum(arr[i])
        results.append(ans)

    # 열 합
    for j in range(100):
        ans2 = sum(arr[i][j] for i in range(100))
        results.append(ans2)


    diag1 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                diag1 += arr[i][j]
    results.append(diag1)

    diag2 = 0
    for i in range(100):
        for j in range(100):
            if i + j == 100 - 1:
                diag2 += arr[i][j]
    results.append(diag2)

    print(f'#{tc} {max(results)}')

