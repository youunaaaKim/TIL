import sys
sys.stdin = open('4843_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    #print(arr)

    big = []
    small = []
    half = len(arr) // 2
    for i in range(half, len(arr)):
        small.append(arr[i])
    for i in range(half):
        big.append(arr[i])
    small.sort()
    result = []
    for i in range(len(small)):
        num1 = big.pop(0)
        num2 = small.pop(0)
        result.append(num1)
        result.append(num2)
    if len(big) != 0:
        num1 = big.pop(0)
        result.append(num1)
    if len(small) != 0:
        num2 = small.pop(0)
        result.append(num2)

    print(f"#{tc}", *result[:10])








