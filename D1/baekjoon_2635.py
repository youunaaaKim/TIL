# 8
# 100 62 38 24 14 10 4 6



input = 100
answer = []
su = 0
for i in range(input-1, 0, -1):
    temp = [input, i]
    while True:
        next_num = answer[i] - answer[i-1]
        if next_num < 0:
            break
        temp.append(next_num)

        if len(temp) > max_len:
            max_len = len(temp)
            answer = temp

    print(max_len)
    print(*answer)




    third = input - next_number
    fourth = next_number - third




print(su)
print(answer)


