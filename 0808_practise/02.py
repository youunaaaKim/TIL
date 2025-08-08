import sys

sys.stdin = open('02_input.txt')

T = int(input())
print(T)

for tc in range(T):
    arr = input()
    # print(arr)
    arr_slicing = arr[::-1]  # 역순으로 바꾸기

    if arr == arr_slicing:  # 원래대로 출력과 역순으로 출력이 같으면
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')