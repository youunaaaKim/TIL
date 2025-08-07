N = 3
card = [4, 5, 6]
#반복문을 활용한 순열

for i in range(N):
    for j in range(N):
        if j != i :
            for k in range(N):
                if k != j and k != i:
                    print(card[i], card[j], card[k])