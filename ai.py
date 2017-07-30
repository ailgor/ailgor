# -- coding: utf-8 --

import random

from qlearning import QLearning

class AI:

	def __init__(self, agent, learningRate, gamma):
		self.agent = agent
		self.learningRate = learningRate
		self.qlearning = QLearning(self.agent.status, self.agent.actions, gamma)
		self.iterations = 0

	def think(self):
		if self.agent.currentStatus == self.agent.targetStatus:
			self.agent.currentStatus = 's1'
			self.iterations += 1
		statusFrom = self.agent.currentStatus
		action = self.map()
		self.agent.execute(action)
		reward = self.agent.getFitness()
		statusTo = self.agent.currentStatus
		self.qlearning.learn(statusFrom, action, statusTo, reward)		

	def map(self):
		action = self.qlearning.optimus(self.agent.currentStatus)
		reward = self.qlearning.reward(self.agent.currentStatus, action)
		explore = random.randrange(0, 100)
		if reward == 0 or explore > (self.learningRate * 100):
			actions = self.agent.getAvailableActions()
			i = random.randrange(0, len(actions))
			action = actions[i]
		return action