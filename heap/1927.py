# 1927번 - 최소 힙

import sys; s=sys.stdin.readline

heap = [0]*200005 # 넣을 수 있는 데이터가 최대 100000개 이므로 큐의 크기를 넉넉히
last = 0

def insert(x):
	global last
	last += 1
	i = last
	while i > 1 and x < heap[i//2]:
		heap[i] = heap[i//2]
		i //= 2
	heap[i] = x
	
def delete():
	global last
	if last == 0:
		return 0
		
	i = 1
	res = heap[i]
	heap[i] = heap[last]
	heap[last] = 0
	last -= 1
	while True:
		cur = i*2
		if heap[i*2+1] != 0 and heap[i*2] > heap[i*2+1]:
			cur += 1
			
		if heap[cur] == 0 or heap[cur] > heap[i]:
			break
		
		temp = heap[cur]
		heap[cur] = heap[i]
		heap[i] = temp
		i = cur
		
	return res

for _ in range(int(s())):
	num = int(s())
	if num == 0:
		print(delete())
	else:
		insert(num)