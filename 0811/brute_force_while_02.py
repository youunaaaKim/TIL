# while 2

def brute_force_while2(p, t):
    '''
    고지식한 알고리즘(Brute Force) - while문 2번째 구현
    t[i]와 p[j]가 다를 경우,
    i를 (현재 i - j + 1)로 조정하고 j=0으로 되돌린 뒤 다시 비교
    '''
    i = 0  # 텍스트 t의 인덱스
    j = 0  # 패턴 p의 인덱스

    while i < N and j < M:
        # 불일치시 i = i - j + 1 즉 패턴 매칭 시작 위치를 한 칸 뒤로 이동 => j = 0 으로 초기화
        # 이 방식은 코드가 조금 더 직관적인 편
        #(“이미 비교한 만큼 뒤로 돌아가고 +1”)
        if t[i] != p[j]:
            # 불일치 시, (i - j + 1)로 이동
            # 이미 비교했던 자리만큼 뒤로 돌아가고, 시작 인덱스를 1 증가
            i = i - j + 1
            # 패턴 인덱스는 0부터 다시 시작
            j = 0
        else:
            # 일치하면 두 인덱스 모두 증가
            i += 1
            j += 1

    if j == M:
        return i - j  # 패턴의 시작 위치
    else:
        return -1  # 검색 실패


print(brute_force_while2(p, t))