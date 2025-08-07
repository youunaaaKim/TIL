import sys
sys.stdin = open('prime_factor.txt')  # input.txt 파일에서 입력을 읽도록 설정

T = int(input())
for tc in range(1, T):
    arr = int(input())
    print(arr)
    i = 2  # 나눌 수를 2로 지정
    while arr > 1:
        if arr % i == 0:
            arr = arr // i
            print(i)
        else:
            i += 1