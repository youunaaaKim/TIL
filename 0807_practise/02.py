import sys
sys.stdin = open('02_input.txt')

# 전체 책 페이지에서 목표 페이지를 찾는 이진 함수
def binary_search_page(pages, goal):
    left = 1
    right = pages
    count = 0 # 이진값을 찾으면서 몇 번만에 찾았는지 세기
    while left <= right:
        count += 1
        mid = (left + right) // 2
        if mid == goal:
            return count # 목표값을 찾으면 몇 번만에 찾았는지 리턴
        elif mid > goal:
            right = mid
        else:
            left = mid
    return -1 # 못찾았을 경우 -1 출력

# 입력 처리
T = int(input())

for tc in range(1, T+1):
    N, A, B = map(int, input().split())

    cnt_a = binary_search_page(N, A)
    cnt_b = binary_search_page(N, B)

    if cnt_a < cnt_b: # 몇 번만에 찾았는지 비교
        winner = 'A'
    elif cnt_b < cnt_a:
        winner = 'B'
    else:
        winner = 0

    print(f"#{tc} {winner}")


