class Stack:
    def __init__(self, size):
        self.size = size  # 스택 크기 저장
        self.capacity = [None] * size  # 고정 크기 배열 사용
        self.top = -1  # 초기 top 포인터는 -1

    def push(self, item):
        if self.top >= self.size - 1:
            return "Stack Overflow"  # 스택이 가득 찬 경우
        self.top += 1
        self.capacity[self.top] = item  # top 위치에 값 저장

    def is_empty(self):
        return self.top == -1  # top 포인터가 -1이면 스택이 비어 있음

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        item = self.capacity[self.top]
        self.capacity[self.top] = None  # top 위치의 값 제거
        self.top -= 1  # top 포인터 감소
        return item

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.capacity[self.top]  # top 위치의 값 반환


# 사용 예제
stack = Stack(3)
stack.push(5)
stack.push(10)
stack.push(15)
print(stack.push(100))  # Stack Overflow
print(stack.pop())  # 15
print(stack.pop())  # 10
print(stack.pop())  # 5
print(stack.pop())  # Stack Underflow