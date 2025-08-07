# SWEA - 1970(쉬운 거스름돈) 참고
# 0~9 숫자 카드에서 임의의 카드 6장을 뽑았을 때
# 3장의 카드가 연속적인 번호를 갖는 경우를 run 이라하고,
# 3장의 카드가 동일한 번호를 갖는 경우를 triple 라고 함.
# 6장의 카드는 run, triple로만 이루어져 있어야 Baby-gin임

num = 456789  # Baby Gin 확인할  6자리 수
c = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
#아니 왜 K+1아님 시부레 10이어야지



for i in range(6):
    c[num % 10] += 1 # 1의 자리에 해당하는 자리에 count 늘리기 (c[9] += 1)
    num //= 10 # 위에서 처리한 1의 자리에 해당하는 숫자 제거

i = 0
tri = run = 0

while i < 10:
    if c[i] >= 3:  # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:  # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print('Baby Gin')
else:
    print('Lose')