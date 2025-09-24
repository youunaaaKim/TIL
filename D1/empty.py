import sys
from collections import deque

sys.stdin = open('1244_input.txt')

def bfs(number, change):
    visited = set()
    q = deque()

    start = ''.join(number)
    q.append((start, change))
    visited.add((start, change))

    max_val = 0

    while q:
        current, cnt = q.popleft()

        if cnt == 0:
            max_val = max(max_val, int(current))
            continue

        current_list = list(current) # 이해 안됨
        n = len(current_list)
        for i in range(n):
            for j in range(1+i, n):
                current_list[i], current_list[j] = current_list[j], current_list[i]
                new_num = "".join(current_list)
                state = (new_num, cnt - 1)  # 새로운 상태 (숫자판, 남은 교환횟수)

                if state not in visited:
                    visited.add(state)
                    q.append(state)
                    # 원상복구 (다음 swap을 위해 다시 돌려놓기)
                    current_list[i], current_list[j] = current_list[j], current_list[i]

                return max_val

            T = int(input())
            for tc in range(1, 1 + T):
                number, change = map(int, input().split())
                number = list(str(number))  # 숫자를 리스트로 변환 (교환 쉽게 하기 위해)
                answer = bfs(number, change)
                print(f"#{tc} {answer}")