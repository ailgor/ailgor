# -- coding: utf-8 --

from agent import Agent
from ai import AI

agent = Agent()
ai = AI(agent, 0.7, 0.5)

while ai.iterations < 8:
	ai.think()
	print '--------------------'
	print 'Iteration',ai.iterations
	print (ai.qlearning.qtable)

print 'Pi*(s1):', ai.qlearning.optimus('s1')
print 'Pi*(s2):', ai.qlearning.optimus('s2')
print 'Pi*(s3):', ai.qlearning.optimus('s3')