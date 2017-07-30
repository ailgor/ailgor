# -- coding: utf-8 --

import numpy as np

class QLearning:

	def __init__(self, status, actions, gamma):
		self.status = status
		self.actions = actions
		self.gamma = gamma
		self.qtable = np.zeros((len(status), len(actions)));

	def learn(self, statusFrom, action, statusTo, rsa):
		iSi = self.status.index(statusFrom)
		iA = self.actions.index(action)
		iSf = self.status.index(statusTo)
		qsa = self.qtable[iSi][iA]
		self.qtable[iSi][iA] = rsa + self.gamma * max(self.qtable[iSf, :])

	def optimus(self, status):
		iS = self.status.index(status)
		iA = np.argmax(self.qtable[iS])
		return self.actions[iA]

	def reward(self, status, action):
		iS = self.status.index(status)
		iA = self.actions.index(action)
		return self.qtable[iS][iA]