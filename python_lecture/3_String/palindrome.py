'''
길이가 4인 회문을 찾는 예
4
CBBCABBA
'''

N = int(input())
txt = input()
total = 0
for j in range(8-N+1):      # 회문을 확인하는 구간의 첫 글자 인덱스
    for k in range(N//2):   # 회문의 길이 절반만큼 비교
        if txt[j+k] != txt[j+N-1-k]:
            break   # 비교 글자가 다르면 현재구간 중지
    else:       # break에 걸리지 않고 for 종료, 회문이면
        total += 1
print(total)