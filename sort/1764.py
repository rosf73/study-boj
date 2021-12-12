##################
# 1764번 # 듣보잡 #
##################

import sys; s=sys.stdin.readline

data = list(map(int, s().split()))

def mergesort(arr, l, r):
	if l == r: return
	
	mid = int((l+r)/2)
	mergesort(arr, l, mid)
	mergesort(arr, mid+1, r)
	
	lidx = l
	ridx = mid+1
	tmp = []
	while lidx <= mid and ridx <= r:
		if arr[lidx] <= arr[ridx]:
			tmp.append(arr[lidx]); lidx += 1
		else:
			tmp.append(arr[ridx]); ridx += 1
			
	while lidx <= mid:
		tmp.append(arr[lidx]); lidx += 1
	while ridx <= r:
		tmp.append(arr[ridx]); ridx += 1
	
	for i in range(len(tmp)):
		arr[l+i] = tmp[i]

people = []
for i in range(data[0]+data[1]):
	person = s().strip()
	people.append(person)

mergesort(people, 0, len(people)-1)
sum = 0
res = []
for i in range(len(people)-1):
	if people[i] == people[i+1]:
		sum += 1
		res.append(people[i])
print(sum)
for e in res:
	print(e)