import sys
sys.stdin = open('1859_input.txt')

T = int(input()) # 테스트케이스
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(arr)

    # 구매리스트
    buy = []
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            buy.append([arr[i], i+1])

        else: # 0부터 시작했을 때 끊겼다면, 다시 시작하기
            for j in range(i+2, len(arr) - 1):
                if arr[j] < arr[j + 1]:
                    buy.append([arr[i], i+1])

    # 쓴 돈 산출
    print(buy)
    total = 0
    spend = 0
    for i in buy:
        spend += i
    print(spend)

    # 판 돈 산출
    price = len(buy)
    benefit = 0
    benefit = arr[price]
    print(benefit)

    total = benefit * price - spend
    print(total)


    #     output = arr[i+1]
    #     total = output - input
    #
    # print(total)



