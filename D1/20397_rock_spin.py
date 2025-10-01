import sys
sys.stdin = open('20397_input.txt')

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        i = i - 1

        for n in range(1, j+1):
            if i-n >= 0 and i+n < N:
                if arr[i-n] == arr[i+n]:
                    arr[i-n] = 1 - arr[i-n]
                    arr[i+n] = 1 - arr[i+n]

    print(f"#{t}", end=" ")
    print(*arr)
