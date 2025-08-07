def counting_sort(input_arr, k):
    counting_arr = [0] *(k+1)

    for num in input_arr:
        counting_arr[num] +=1


    for i in range(1, k+1):
        counting_arr[i] +=counting_arr[i-1]

    result_arr = [0] * len(input_arr)
    for i in range(len(input_arr)-1, -1, -1):
        counting_arr[num] -=1
        result_arr[counting_arr[num]] = num
    return result_arr



