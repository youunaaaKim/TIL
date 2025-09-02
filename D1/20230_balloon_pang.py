import sys
sys.stdin = open('20230_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_boom = 0

    for r in range(N):
        for c in range(N):
            row_sum = sum(arr[r])  # r행의 합
            col_sum = sum(arr[i][c] for i in range(N))  # c열의 합
            total = row_sum + col_sum - arr[r][c]  # 중복 칸 제거
            if total > max_boom:
                max_boom = total

    print(max_boom)




    #         row_sum = 0
    #         for i in range(N):
    #             row_sum += arr[r][i]
    #
    #         col_sum = 0
    #         for j in range(N):
    #             col_sum += arr[j][c]
    #
    #         total = row_sum + col_sum - arr[r][c]  # 중복 칸 제거
    #         if total > max_boom:
    #             max_boom = total
    #
    # print(max_boom)