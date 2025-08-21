import sys
sys.stdin = open('sdoku.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(1, 9)]
    # print(arr)

    # 열과 행을 돌아가며 숫자 겹치는거 있는지 찾기
    for r in arr:
        c = [0] * 12  # 숫자 개수 저장용 리스트
        for num in r:
            c[num] += 1
            if c[num] >= 2:
                print(0)

    for col in zip(*arr):
        c = [0] * 12
        for num in col:
            c[num] += 1
            if c[num] >= 2:
                print(0)




    # 3*3 도 보기
    # for r in range():





