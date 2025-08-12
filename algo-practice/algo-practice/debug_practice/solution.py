import sys

sys.stdin = open('input.txt')

T = int(input())


def solve(N):
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                boxes[i][j] += color


for tc in range(1, T + 1):
    boxes = [[0] * 10 for _ in range(10)]
    N = int(input())
    cnt = 0

    solve(N)

    for i in range(10):
        for j in range(10):
            if boxes[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
