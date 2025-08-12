import sys

sys.stdin = open('input.txt')


# 1 2 3 4 5 => [1, 2, 3, 4, 5]
numbers = list(map(int, input().split()))

print(numbers)
