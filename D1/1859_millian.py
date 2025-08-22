import sys
sys.stdin = open('1859_input.txt')

def max_profit(prices):
    max_price = 0
    profit = 0

    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price # 현재가가 최고가보다 낮으면, 차익만큼 이익 발생
    return profit

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    result = max_profit(prices)
    print(f"#{tc} {result}")

