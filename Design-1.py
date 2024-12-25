
######## Design a Hash Set ###########

class HashSet:
	def __init__(self):
		self.columns= [None] * 1000
		
	def add(self, key):
		column_num = key % 1000
		if self.columns[column_num] == None:
			self.columns[column_num] = [False]*1001
		row_num = key / 1001
		self.columns[column_num][row_num] = True
		
	def remove(self, key):
		column_num = key % 1000
		if self.columns[column_num] == None:
			return 
		row_num = key / 1001
		self.columns[column_num][row_num]  = False
		
	def contains(self, key):
		column_num = key % 1000
		if self.columns[column_num] == None:
			return False
		row_num = key / 1001
		return self.columns[column_num][row_num]

######## Design a Min Stack Data Structure ###########

class MinStack:

	def __init__(self):
		self.stack = []
		self.currMin = float('inf')

	def push(self, value):
		if value <= self.currMin:
			self.stack.append(self.currMin)
			self.currMin = value
		self.stack.append(value)
	
	def pop(self):
		if self.stack[-1] > self.currMin:
			return self.stack.pop()
		else:
			value = self.stack.pop()
			self.currMin = self.stack.pop()
			return value

	def getMin(self):
		return self.currMin
	
	def top(self):
		return self.stack[-1]
