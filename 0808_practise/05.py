import sys
sys.stdin = open('05_input.txt')
T = int(input())          # 첫 줄은 테스트케이스 수

for tc in range(1, 1+T):
    arr = [input() for _ in range(5)]
    print(arr)

    for i in range(len(arr)):
        for j in range(len(arr[i])):  # ✅ i번째 문자열의 길이
            print(arr[i][1])  # i번째 줄의 j번째 문자