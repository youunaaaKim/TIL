import sys
sys.stdin = open('03_input.txt')

T = 10

for tc in range(1, T+1):
    L = int(input().strip())
    arr = [list(input().strip()) for _ in range(8)]

    hwemoon_count = 0

    # 가로 탐색
    for r in range(8):
        row = arr[r]
        for i in range(0, 8 - L + 1):
            if row[i:i+L] == row[i:i+L][::-1]:
                hwemoon_count += 1

    # 세로 탐색
    for c in range(8):
        col = [arr[r][c] for r in range(8)]
        for i in range(0, 8 - L + 1):
            if col[i:i+L] == col[i:i+L][::-1]:
                hwemoon_count += 1

    print(f'#{tc} {hwemoon_count}')

