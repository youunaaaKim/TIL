def backtrack(idx, subset):
    """
    부분집합을 백트래킹으로 탐색
    현재까지 선택한 부분집합의 합이 target이면 result에 추가

    idx: nums 리스트의 인덱스 위치
    subset: 부분집합

    코드 실행 부분(합이 10이 되는지. 되면 보관)과 부분집합 만드는
    """
