import sys
sys.stdin = open('5431_homework_input.txt')
T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N: 수강생의 수, K : 과제를 제출한 사람의 수
    arr = list(map(int, input().split())) # 과제를 제출한 사람의 번호 K개
    #print(arr)

    # 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하기
    # arr에 없는 숫자를 빼서 오름차순 정렬하기

    # 학생 배열 만들기
    student = [0] * (N+1)
    for i in arr:
        student[i] += 1
    #print(student)

    # 숫제를 안한 사람의 숫자 리스트
    name = []
    for stu in range(1, len(student)):
        if student[stu] == 0:
            name.append(stu)

    print(f"#{tc}", *name)










