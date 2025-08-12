class Stack:
    def __init__(self):
        self.stack = []  # 리스트를 스택으로 사용

    def push(self, value):
        self.stack.append(value)  # 리스트의 append()를 활용

    def pop(self):
        if self.is_empty():
            return "스택이 비었습니다~!~!~!~!~!"
        return self.stack.pop()  # pop()을 사용하여 제거

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]  # 마지막 요소 반환

    def is_empty(self):
        return len(self.stack) == 0  # 리스트가 비었는지 확인

# 사용 예제
s = Stack()
s.push("김")
s.push("유")
s.push("나")
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())   # Stack is empty