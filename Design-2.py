############## Design Queue using Stack ##############

class Queue:
	def __init__(self):
		self.in_stack = []
		self.out_stack = []

	def push(self, value):
		self.in_stack.append(value)

	def pop(self):
		if not self.out_stack:
			while self.in_stack:
				self.out_stack.append(self.in_stack.pop())
		return self.out_stack.pop()

	def peek(self):
		if not self.out_stack:
			while self.in_stack:
				self.out_stack.append(self.in_stack.pop())
		return self.out_stack[-1]

	def isEmpty(self):
		return not self.in_stack and not self.out_stack

############## Design Hashmap ##############

class HashMap:

    def __init__(self):
		  self.columns= [None] * 1000

    def put(self, key, value):
		  column_num = key % 1000
		  if self.columns[column_num] == None:
			  self.columns[column_num] = [-1]*1001
		  row_num = key / 1001
		  self.columns[column_num][row_num] = value

    def remove(self, key):
		  column_num = key % 1000
		  if self.columns[column_num] == None:
			  return 
		  row_num = key / 1001
		  self.columns[column_num][row_num]  = -1

    def get(self, key):
		  column_num = key % 1000
		  if self.columns[column_num] == None:
			  return -1
		  row_num = key / 1001
		  return self.columns[column_num][row_num]

