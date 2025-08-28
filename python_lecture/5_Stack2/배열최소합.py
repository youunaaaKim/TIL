'''
10
6 9 1 4 1 2 2 3 2 9
3 9 3 5 6 7 6 5 7 5
9 9 8 9 5 5 2 8 4 3
3 7 7 6 8 3 4 6 4 3
3 3 2 4 2 2 2 8 8 7
9 5 4 1 8 1 2 6 6 3
3 7 7 2 3 2 2 2 3 4
9 5 9 5 2 1 4 7 7 4
6 8 1 8 3 3 1 2 9 1
4 6 7 5 8 3 8 5 4 2

20 9864101
'''
def f(i, N, s):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v
    global cnt
    cnt += 1

    if i == N:  #
        if min_v > s:
            min_v = s
    elif min_v < s: # 중간 합계가 최소합보다 크면
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]     # 자리교환
            f(i+1, N, s + arr[i][p[i]])   # i+1자리 결정
            p[i], p[j] = p[j], p[i]     # 원상복구


N = int(input())    # 배열의 크기 N x N
arr = [list(map(int, input().split())) for _ in range(N)]

p = [ i for i in range(N) ] # P[i] : i에서 고른 열 번호
min_v = 10000
cnt = 0
f(0, N, 0)
print(min_v, cnt)