# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
# [입력]
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
import sys
sys.stdin = open('sample_output.txt')

T = int(input()) #테스트 케이스의 수
# print(T)
for tc in range(1, T+1): # 1부터 T까지 반복
    N = int(input()) #테스트 케이스의 첫 번째 숫자(수의 개수 N)
    # 공백으로 구분된 숫자들을 정수로 변환하고,리스트로 저장하기
    arr = list(map(int, input().split()))
    # print(N)
    # print(row)

    #첫 번째 수를 최댓값과 최솟값으로 설정
    max_num = arr[0]
    min_num = arr[0]
    #리스트를 돌면서 최댓값과 최솟값 갱신
    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    # 최대값과 최소값의 차이 구하기
    answer = max_num - min_num
    print(f'#{tc} \n{answer}')



#output
#1 630739
#2 740510
#3 838110