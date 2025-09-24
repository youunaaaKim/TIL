from collections import deque
import sys

sys.stdin = open('1244_input.txt')


def bfs(number, change):
    visited = set() # 방문 기록: (숫자 문자열, 남은 교환 횟수) 형태로 저장
    q = deque() # 큐에는 (현재 숫자 상태, 남은 교환 횟수)를 저장

    start = "".join(number)
    q.append((start, change))
    visited.add((start, change))

    max_value = 0  # 최댓값을 저장할 변수

    while q:
        current, cnt = q.popleft()

        # 교환 횟수를 다 썼으면 최댓값 후보로 비교
        if cnt == 0:
            max_value = max(max_value, int(current))
            continue

        current_list = list(current)
        n = len(current_list)
        for i in range(n):
            for j in range(i+1, n):
                # 두 자리 교환
                current_list[i], current_list[j] = current_list[j], current_list[i]
                new_num = "".join(current_list)
                state = (new_num, cnt - 1)  # 새로운 상태 (숫자판, 남은 교환횟수)

                # 이미 같은 상태를 방문했으면 다시 큐에 넣을 필요 없음
                if state not in visited:
                    visited.add(state)
                    q.append(state)

                # 원상복구 (다음 swap을 위해 다시 돌려놓기)
                current_list[i], current_list[j] = current_list[j], current_list[i]



    return max_value


T = int(input())
for tc in range(1, 1+T):
    number, change = map(int, input().split())
    number = list(str(number))  # 숫자를 리스트로 변환 (교환 쉽게 하기 위해)
    answer = bfs(number, change)
    print(f"#{tc} {answer}")