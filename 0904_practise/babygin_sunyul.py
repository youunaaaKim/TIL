import sys
from itertools import permutations

sys.stdin = open('babygin_input.txt')


def is_run(cards):
    """ run인지 확인하는 함수  """
    # 인덱스 위치 값이 1씩 증가함에 따라 인덱스에 해당하는 값이 1씩 증가하는지 확인
    return cards[0] + 1 == cards[1] and cards[1] + 1 == cards[2]


def is_triplet(cards):
    """ triplet인지 확인하는 함수 """
    # 세 장의 카드가 모두 같은지 확인
    return cards[0] == cards[1] == cards[2]


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input()))
    is_babygin = False #베이비진인지 확인하는 초기값은 false

    # 순열 생성
    # set으로 중복된 순열을 제거하기
    for p in set(permutations(cards)): # permutations 모든 순열을 만들어 줌
        # 앞 3장과 뒤 세장으로 나누고 이를 정렬
        group1 = sorted(list(p[:3]))
        group2 = sorted(list(p[3:]))

        # run or triplet인지 확인합니다.
        check1 = is_run(group1) or is_triplet(group1)
        check2 = is_run(group2) or is_triplet(group2)

        # 두 조건을 만족하면 베이비진 출력
        if check1 and check2:
            is_babygin = True
            break  # 하나라도 찾으면 더 이상 탐색할 필요가 없습니다.

    print(f'#{tc} {is_babygin}')