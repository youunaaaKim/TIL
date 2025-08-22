'''
연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.
'''
import sys
sys.stdin = open('9836_input')

T = int(input()) # 테스트케이스
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().strip()))

    count = 0
    max_count = 0
    for i in arr:
        if i == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    print(max_count)



