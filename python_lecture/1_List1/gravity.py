'''
9
7 4 2 0 0 6 0 7 0
=> 7
9
4 2 0 0 7 6 0 7 0
=> 5
'''

N = int(input())
box = list(map(int, input().split()))

max_v = 0
for i in range(N-1):
    cnt = 0         # i박스 오른쪽(i+1~N-1)에 더 낮은 박스 개수 (낙차)
    for j in range(i+1, N):
        if box[i] > box[j]:
            cnt += 1    # 더 낮은 박스면 낙차 추가
    if max_v < cnt:
        max_v = cnt
print(max_v)