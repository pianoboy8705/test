import scipy as sp
import math

def OldRandomGenerator(seed,outputLength,a,b,M):

	outputVec = sp.zeros(outputLength)
	outputVec[0] = seed
	for i in range(outputLength-1):
		outputVec[i+1] = sp.mod(a*outputVec[i] + b,M)

	return outputVec
	
	
def ShuffleTest():
	seedVec = sp.arange(12345,12400)
	outputMatrix = sp.zeros([seedVec.size,6])
	i = 0
	for seed in seedVec:
		test = OldRandomGenerator(seed,54,7**5,0,2**31-1)
		testshuffle = sp.argsort(test[2:test.size])
		outputMatrix[i,:] = testshuffle[0:6]
		i +=1
	
	return outputMatrix
	
	#This is a change for Git