def f(i, N, V): # i 배열 인덱스, N 배열크기, V 찾는 값
    if i==N:    # V가 없는 경우  (배열을 벗어남)
        return 0
    elif A[i] == V: # 찾은 경우
        return 1
    else:  # 재귀호출
        return f(i+1, N, V)

N = 3
A = [3, 7, 6]
#V = 2
V = 6
ans = f(0, N, V)
print(ans)
# print(f(0, N, V))