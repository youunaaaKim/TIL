t = 'A pattern matching algorithm'
p = 'rithm'

N = len(t)  # 전체 텍스트 길이
M = len(p)  # 패턴 길이


def brute_force_for(p, t):
    '''
    고지식한 알고리즘(Brute Force) - for문 구현
    텍스트를 순회하며 패턴의 각 문자와 일치 여부를 확인
    '''
    N = len(t)
    M = len(p)

    # i: 텍스트에서 패턴이 시작될 수 있는 모든 위치를 순회
    for i in range(N - M + 1):
        cnt = 0
        # j: 패턴 내부를 순회하며 매칭 확인
        for j in range(M):
            if t[i + j] == p[j]:
                cnt += 1
            else:
                # 불일치 발생 시, 내부 반복 탈출
                break

        # cnt가 M과 같다면 패턴 전체가 일치
        if cnt == M:
            return i

    # 패턴을 찾지 못한 경우
    return -1


print(brute_force_for(p, t))