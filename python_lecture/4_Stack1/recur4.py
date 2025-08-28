# 재귀로 부분집합 만들기

def f(i, N):
    if i == N:  # 배열을 벗어나면
        print(*A, end = ' : ')
        for j in range(N):
            if A[j]:
                print(B[j], end =' ')
        print()
    else:
        A[i] = 0
        f(i+1, N)
        A[i] = 1
        f(i+1, N)
N = 3
A = [0] * N
B = [1,2,3]
f(0, N)