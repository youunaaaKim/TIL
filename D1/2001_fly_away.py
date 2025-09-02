import sys
sys.stdin = open('2001_fly_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    N = int(N)
    M = int(M)
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    max_kill = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            total = 0
            for i in range(M):
                for j in range(M):
                    total += arr[r+i][c+j]
            if total > max_kill:
                max_kill = total

    print(f'#{tc} {max_kill}')