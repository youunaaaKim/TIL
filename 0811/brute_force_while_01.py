# 전체 텍스트
t = 'A pattern matching algorithm'
# 검색할 패턴
p = 'rithm'

N = len(t)  # 전체 텍스트의 길이
M = len(p)  # 찾을 패턴의 길이


def brute_force_while1(p, t):
    '''
    고지식한 알고리즘(Brute Force) - while문 1번째 구현
    t[i]와 p[j]가 다를 경우,
    i를 (현재 i - j)로 되돌린 뒤 j를 -1로 만들어 재정렬하는 방식
    '''
    i = 0  # 텍스트 t의 인덱스
    j = 0  # 패턴 p의 인덱스

    while i < N and j < M:
        # 불일치 시 i = i - j 로 i 위치를 과거로 되돌린 뒤,
        # j = -1 로 만들어 다음 루프에서 j가 0이 되도록 설정
        # `i - M` 가 곧 패턴 시작 인덱스
        if t[i] != p[j]:
            # 불일치 시, 비교 시작 위치를 한 칸씩 앞으로 이동
            # (i - j): 패턴을 처음부터 다시 비교해야 하므로
            i = i - j
            # j를 -1로 만들고, 바로 아래서 j += 1 → j=0
            j = -1
        i += 1
        j += 1

    # while 문을 빠져나온 상태에서,
    # j가 M과 같다면 패턴을 모두 일치시킨 것
    if j == M:
        return i - M  # 패턴이 일치한 시작 인덱스
    else:
        return -1  # 검색 실패


print(brute_force_while1(p, t))