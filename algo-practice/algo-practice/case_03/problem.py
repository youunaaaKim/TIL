import sys

sys.stdin = open('input.txt')

N = int(input())

# 1
number_list = []
for _ in range(N):
    row = list(map(int, input().split()))
    number_list.append(row)

# 2
# number_list = [list(map(int, input().split())) for _ in range(N)]

print(number_list)
