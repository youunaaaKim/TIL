#패턴이 몇 번 등장하는지를 세는 기능을 추가한 코드

def brute_force_while2_count(p, t):
    '''
    고지식한 문자열 검색(Brute Force) - while문(두 번째 버전)에
    "패턴이 몇 번 등장하는지"를 세는 기능을 추가한 코드.

    - p: 패턴
    - t: 전체 텍스트
    - 반환값: p가 t 내에서 몇 번 등장하는지 나타내는 정수
    '''
    N = len(t)
    M = len(p)

    i = 0  # 텍스트 t 인덱스
    j = 0  # 패턴 p 인덱스
    count = 0  # 패턴 등장 횟수 누적

    # 텍스트 전체를 끝까지 순회
    while i < N:
        # 만약 문자가 일치하면
        if j < M and t[i] == p[j]:
            i += 1
            j += 1

            # 패턴 전체를 매칭한 경우 (j == M)
            if j == M:
                count += 1  # 등장 횟수 증가
                # 다음 위치로 진행 (겹치는 패턴도 검사 가능하도록)
                # 가장 간단한 방식: 패턴 재시작 (j=0), 그리고 현재 i 위치에서 계속
                j = 0
        else:
            # 불일치 시
            i = i - j + 1  # 시작 위치를 한 칸 뒤로
            j = 0  # 패턴 인덱스 리셋

    return count


text = "ababcabcababc"
pattern = "abc"

result = brute_force_while2_count(pattern, text)
print(f"'{pattern}' 패턴은 '{text}'에서 총 {result}번 등장")