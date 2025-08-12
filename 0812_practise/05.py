# 2005. 파스칼의 삼각형
import sys
sys.stdin = open('05_input.txt')
pascal = [
"1",
"1 1",
"1 2 1",
"1 3 3 1",
"1 4 6 4 1",
"1 5 10 10 5 1",
"1 6 15 20 15 6 1",
"1 7 21 35 35 21 7 1",
"1 8 28 56 70 56 28 8 1",
"1 9 36 84 126 126 84 36 9 1"
]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(f"#{test_case}")
    for i in range(N):
        print(pascal[i])

