n = int(input())
max_len = 0
final_seq = []

for i in range(n, 0, -1):
    seq = [n, i]
    while True:
        next_num = seq[-2] - seq[-1]
        if next_num < 0:
            break
        seq.append(next_num)
    if len(seq) > max_len:
        max_len = len(seq)
        final_seq = seq

print(max_len)
print(*final_seq)
