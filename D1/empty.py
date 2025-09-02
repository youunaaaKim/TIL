import sys
sys.stdin = open('20230_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for r in range(N):
        for c in range(N):
            total = 0
            row_sum = sum(arr[r])
            col_sum = sum(arr[i][c] for i in range(N))

            total = row_sum + col_sum - arr[r][c]
            if total > answer:
                answer = total

    print(answer)