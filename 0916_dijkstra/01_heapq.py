import heapq

# --- 1. heappush와 heappop ---
# 힙으로 사용할 빈 리스트 생성
heap = []

# 힙에 원소 추가: heapq.heappush(heap_list, item)
# 추가할 때마다 리스트는 최소 힙 속성을 유지하도록 재정렬됨
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
print(f"원소 3개 추가 후 heap: {heap}")  # 항상 heap[0]이 최솟값

# 힙에서 가장 작은 원소 꺼내기: heapq.heappop(heap_list)
smallest = heapq.heappop(heap)
print(f"꺼낸 최솟값: {smallest}")
print(f"pop 이후 heap: {heap}")


print('--------------------------------')


# --- 2. heapify ---
# 이미 원소가 있는 리스트
arr = [5, 3, 8, 4, 1, 2]
print(f"원본 리스트: {arr}")

# 기존 리스트를 제자리에서 한 번에 힙으로 변환
heapq.heapify(arr)
print(f"heapify 적용 후: {arr}")

# heapify된 리스트에서 원소를 꺼내면 역시 최솟값부터 나옴
print(f"heapify 후 pop: {heapq.heappop(arr)}")
print(f"heapify pop 이후: {arr}")


print('--------------------------------')


# --- 3. 우선순위 큐 ---
tasks = []
# (우선순위, 할 일)
heapq.heappush(tasks, (3, "보고서 쓰기"))
heapq.heappush(tasks, (1, "긴급 이메일 확인"))
heapq.heappush(tasks, (2, "회의 슬라이드 작성"))

# 우선순위가 가장 낮은 숫자(=가장 높은 우선순위)가 먼저 pop됨
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"[우선순위 {priority}] {task}")
