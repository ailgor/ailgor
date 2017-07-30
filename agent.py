# -- coding: utf-8 --

class Agent:

	def __init__(self):
		self.name = "Machin Status"
		self.actions = ['a1', 'a2', 'a3']
		self.status = ['s1', 's2', 's3', 's4']
		self.currentStatus = 's1'
		self.targetStatus = 's4'
		self.transitions = {'s1':
								{'a1': 's2', 'a2': 's3'}
							, 's2':
								{'a1': 's1', 'a2': 's4', 'a3': 's3'}
							, 's3':
								{'a2': 's2', 'a3': 's4'}
							}
		print "Hello, I'm Machin Status"

	def getFitness(self):
		if self.currentStatus == self.targetStatus:
			return 1
		else:
			return 0

	def getAvailableActions(self):
		return self.transitions[self.currentStatus].keys()

	def execute(self, action):
		if (self.transitions[self.currentStatus][action]):
			self.currentStatus = self.transitions[self.currentStatus][action]
