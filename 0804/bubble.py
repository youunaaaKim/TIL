# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-1-i):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr
#
#
# numbers = [64, 13, 9, 62, 3]
# sorted_numbers = bubble_sort(numbers)
# print("정렬 후:", sorted_numbers)
# #output [3, 9, 13, 62, 64]
#

def bubble_sort(arr):
    n = len(arr) #arr의 길이를 n이라고 정의
    for i in range(n-1, 0, -1): #맨 뒤에서 두 번째 에서 0까지 거꾸로 한 단계씩 진행
        for j in range(0, i): # 0부터 i까지 진행
            if arr[j] > arr[j+1]: #j 번째 인덱스와 j+1번째 인덱스 숫자 비교
                arr[j], arr[j+1] = arr[j+1], arr[j] # sort
    return arr #sort 완료된 배열 반환

numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)

