import sys
sys.stdin = open('1244_input.txt')  
T = int(input())  

for tc in range(1, T+1):  
    arr, N = input().split()  # arr는 숫자 문자열, N은 교환 횟수
    N = int(N)  
    arr = list(arr)   # 문자열은 리스트로 바꾸기
    length = len(arr)  # 문자열의 개수
    
    # 중복 계산 방지 중복이라 함은 : (같은 숫자 배열, 교환 횟수) 
    visited = set()

    # 스택에는 (현재 숫자 배열, 지금까지 사용한 교환 횟수) 튜플을 저장
    stack = [(arr, 0)]  # 처음 상태, 교환 횟수 0

    max_result = '0'  # 최댓값 비교를 위해 초기값 0 설정

    while stack:  # 스택이 트루인 동안 -> 스택이 빈공간이 아닌 동안
        now, cnt = stack.pop()  # 현재 상태와 현재까지 사용한 교환 횟수를 꺼냄

        if cnt == N:  # 종료 조건: 교환 횟수가 주어진 교환 횟수와 같으면  결과 비교
            now_str = ''.join(now)    # 리스트를 문자열로 다시 바꾸고
            print(now_str)
            if now_str > max_result: # 현재 결과가 기존 최대값보다 크면
                max_result = now_str  # 더 크면 갱신
            continue  # 더 크지 않으면 지나가기

        # 중복 상태인지 확인 => 중복이라 함은 : (같은 숫자 배열, 교환 횟수) 
        state = (''.join(now), cnt)
        if state in visited:   # 중복 체크
            continue # 이미 본 상태면 중복 계산 방지 위해 건너뜀
        visited.add(state)  # 방문한 상태 기록
        
        # 현재 상태에서 가능한 모든 자리 교환해보기
        for i in range(length): #  i, j를 골라 서로 바꿈
            for j in range(i + 1, length):
                now[i], now[j] = now[j], now[i]  # 자리 바꾸기 (swap)
                print(''.join(now))
                # 바꾼 상태와 사용 교환 횟수 +1을 스택에 저장
                stack.append((now[:], cnt + 1)) # 바꾼 상태와 교환 횟수 +1을 스택에 넣음
                now[i], now[j] = now[j], now[i]  # 다시 원래대로 복원

    print(f'#{tc} {max_result}')  # 모든 경우 탐색 후 최댓값 출력
