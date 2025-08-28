import sys
sys.stdin = open('3499_input.txt')

T = int(input())
for tc in range(1, T+1):
    how_many_card = int(input())
    card_list = list(input().split())
    # print(card_list)

    # 짝수면 반절반절 나눠서 카드 나누기
    first = []
    second = []

    #앞 뒤를 나누기
    half = how_many_card / 2
    half = int(half)


    if how_many_card % 2 == 0:
        first = card_list[:half]
        second = card_list[half:]

        # 번갈아가면서 카드 쌓기
        final_card_list = []
        for i in range(len(second)):
            final_card_list.append(first[i])
            final_card_list.append(second[i])

    else :
        first = card_list[:half+1]
        second =card_list[half+1:]

        # 번갈아가면서 카드 쌓기
        final_card_list = []
        for i in range(len(second)):
            final_card_list.append(first[i])
            final_card_list.append(second[i])
            final_card_list.append(first[i + 1])

    print(f'#{tc} {final_card_list}')

