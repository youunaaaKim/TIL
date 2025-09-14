T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    whitch_max = -1

    for i in range(N):
        for j in range(1+i, N):
            multied = arr[i] * arr[j]

            multied_str = str(multied)
            if len(multied_str) ==1:
                