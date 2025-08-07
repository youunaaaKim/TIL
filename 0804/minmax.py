import sys

sys.stdin = open('sample_output.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for num in arr:
        min_num = arr[0]
        max_num = arr[0]
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    answer = max_num - min_num
    print(answer)


