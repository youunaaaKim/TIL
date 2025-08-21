'''
- 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라 한다.
- 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.
- 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하라.

[입력 예]
- 667767은 두 개의 triplet이므로 baby-gin이다. (666, 777)
- 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin이다.(456, 000)
- 101123은 한 개의 triplet이 존재하나, 023이 run이 아니므로 baby-gin이 아니다. (123을 run으로 사용하더라도  011이 run이나 triplet이 아님)
'''

import sys
sys.stdin = open('baby_input.txt')

T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input()))
    sorted_num = sorted(num)
    # print(num)
    # print(sorted_num)

    c = [0] * 12  # 숫자 개수 저장용 리스트
    for cards in num:
        c[cards] += 1

    triple_count = 0 # 트리플 저장
    run_count = 0 # 런 저장
    # triple 찾기
    for i in range(10):
        # i번 카드가 3장 이상이면
        while c[i] >= 3:
            c[i] -= 3  # 사용한 3장 지우기
            triple_count += 1

    # 남은 카드로 run 찾기
    for i in range(8):
        # i, i+1, i+2 카드가 모두 1장 이상이면 run
        while c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run_count += 1

    # print(triple_count)
    # print(run_count)
    # triple_count + run_count 가 2면 베이비진
    if triple_count + run_count == 2:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')