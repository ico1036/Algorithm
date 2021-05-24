# Linked list
# ex 3 nodes:  67 -> 30 -> 59
# Node: data , link(where is next)

# -- Contents in Linked list 
# Head: First node
# Tail: Last node
# Number of nodes: ex 3


class Node:
	def __init__(sef,item):
		self.data = item
		self.next = None
		

class LinkedList:
	def __init__(self):
		self.nodeCount = 0
		self.head = None
		self.tail = None

# Possible Operation?
# 1. K-th item
# 2. Loop
# 3. length
# 4. Insert
# 5. del
# 6. Merge two list 
	


# We do not use the first index 0
# We use it as index 1

	# 특정원소 지칭 
	def getAt(self,pos):
		if pos <=0 or pos > self.nodeCount
			return None

		else:
			curr = self.head
			while i <pos:
				curr = curr.next
				i+=1
			return curr


# 배열#
# 저장공간 -연속한위치
# 특정원소 지칭: 매우간편 (O(1))
	
# 연결 리스트#
# 저장공간 -임의의 위치
# 특정원소 지칭: 선형탐색 (O(n))




