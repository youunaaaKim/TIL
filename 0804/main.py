def bubble_sort(arr):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)
#output [3, 9, 13, 62, 64]