from collections import deque
queue = deque([10,20,30])
queue.append(40)
print(queue.popleft()) # 10 출력
