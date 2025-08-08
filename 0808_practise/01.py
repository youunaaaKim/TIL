import sys

sys.stdin = open('01_input.txt')

T = int(input())
# print(T)

for tc in range(T):
    arr = input()
    # print(arr)
    word = ''  # 빈 문자열 생성

    for w in arr:
        word = w + word  # 문자열을 하나씩 돌면서 뒤로 붙이기
    print(f'#{tc} {word}')

    # ---------------------------------------------
    # 슬라이싱
    print(arr[::-1])