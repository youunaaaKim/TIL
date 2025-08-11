import sys
sys.stdin = open('01_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(2)]
    print(arr)
    # value가 0인 딕셔너리 만들기
    count_number = dict.fromkeys(arr[0], 0)
    print(count_number)

    # arr[0] 의 인수가 arr[1]에 있으면 count_number의 value 값을 +1
    for i in arr[1]:
        if i in count_number:
            count_number[i] +=1
    print(count_number)

    #딕셔너리 값 중 가장 큰 값 print
    max_number = 0
    for num in count_number:
        if max_number < count_number[num]:
            max_number = count_number[num]
    print(f'#{tc} {max_number}')
