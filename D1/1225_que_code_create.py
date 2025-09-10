import sys

sys.stdin = open('1225_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(arr)

    i=0
    new_num = 0
    while arr[7] > 0: # arr[i]가 0 보다 큰 동안
        for j in range(5):
            num = arr.pop(0) # 0 번째 인덱스 꺼내기
            new_num = num - (j+1) # 싸이클 돌 때마다 다시 빼서 0에서 8까지 하나씩 증가하면서 빼기
            if new_num > 0: # 0 뼀을 때 음수가 아닌 경우에만
                arr.append(new_num)  # 맨 뒤에 다시 넣기
            else: # 0 혹은 음수라면
                new_num = 0 # 0으로 바꿔주고
                arr.append(new_num) # 맨 뒤에 어팬드하고 종료
                break # 와일문 종료
        if new_num == 0: # 포문 종료
            break


    print(f'#{tc} {" ".join(map(str, arr))}')