import sys
sys.stdin = open('sample_number_card')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    empty_arr = [0] * 10
    for i in arr:
        empty_arr[i] += 1

        many_num = -1
        many_count = -1
        for i in range(9, 0, -1):
            if empty_arr[i] > many_num:
                many_num = empty_arr[i]
                many_count = i
    print(f'#{tc} {many_count} {many_num}')


