import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    matrix = []
    N = int(input())

    # 1
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    # 2
    # matrix = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}')
    print(f'{matrix}')
