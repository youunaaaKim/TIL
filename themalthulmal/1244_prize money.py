import sys
sys.stdin = open('1244_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr, N = input().split()
    N = int(N)
    arr = list(arr)
    length = len(arr)

    # visited: 중복 계산 방지 (상태 + depth 기록)
    visited = set()
    stack = [(arr, 0)]  # (현재 상태, depth)
    max_result = '0'

    while stack:
        now, cnt = stack.pop()

        # 종료 조건: 교환 다 했을 때
        if cnt == N:
            now_str = ''.join(now)
            if now_str > max_result:
                max_result = now_str
            continue

        # 중복 상태는 skip
        state = (''.join(now), cnt)
        if state in visited:
            continue
        visited.add(state)

        # 가능한 모든 쌍 swap 시도
        for i in range(length):
            for j in range(i + 1, length):
                now[i], now[j] = now[j], now[i]
                stack.append((now[:], cnt + 1))  # 복사해서 push
                now[i], now[j] = now[j], now[i]  # 원상복구

    print(f'#{tc} {max_result}')
