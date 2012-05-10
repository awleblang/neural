import numpy 
from numpy import *
from pylab import * 

LetterA = array([  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
		   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
		   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
	           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1],
		   [-1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1],
		   [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1],
		   [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1],
		   [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1],
		   [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1],
		   [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1],
		   [-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1],
		   [-1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1],
		   [-1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1],
		   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1],
		   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
		   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
		   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1]])

LetterB = array([ [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, -1, -1, -1, 1, 1, -1, -1, -1, 1],
                  [1, -1, -1, -1, 1, 1, -1, -1, -1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [-1, 1, 1, 1, -1, -1, 1, 1, 1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] ])


LetterC = array([ [-1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, -1, -1, -1, -1, 1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] ])


ArrayofLetters = array([LetterA])
NewLetters = array([LetterB])

L = len(LetterA[0])         #dimension of lattice
N = L**2                    #number of neurons in network
M = len(ArrayofLetters)     #number of stored patterns
M2 = len(NewLetters)


Jarray = zeros((L, L, L, L))
beta = 1.0
for m in range(M):
    Letter = ArrayofLetters[m]
    for i in range(L):
        for j in range(L):
            for k in range(L):
                for l in range(L):
                    Jarray[i, j, k, l] += (beta/M)*(Letter[i, j]*Letter[k, l]) 

J2array = zeros((L, L, L, L))
alpha = 1.0
for m in range(M2):
    Letter = NewLetters[m]
    for i in range(L):
	for j in range(L):
	    for k in range(L):
		for l in range(L):
		    J2array[i, j, k, l] += alpha*Letter[i, j]*Letter[k, l]

NewJarray = Jarray + J2array
    

def damage(n, damaged):
    for i in range(n):
        damaged[int(L*numpy.random.random(1)), int(L*numpy.random.random(1))] *= -1



def monteCarloStep(array):  # nonweave version
	
    randomArray = numpy.random.random([L, L, L, L])  # random number for Metropolis algorithm
    
    randomPositions = L*numpy.random.random(2*N)
    
    for k in range(N):
        
        i = int(randomPositions[2*k])
        j = int(randomPositions[2*k + 1])
        
        dE = 0
        
        for l in range(L):
            for m in range(L):
                
                dE += 2*NewJarray[i, j, l, m]*array[i, j]*array[l, m]
        
        if dE < 0:
            newSpin = -array[i, j]
            array[i, j] = newSpin
    
    """for i in range(L):
        for j in range(L):
            dE = 0
            for k in range(L):
                for l in range(L):
                    dE += 2*NewJarray[i, j, k, l]*array[i, j]*array[k, l]
                                
            if ((dE < 0)):
                newSpin = -array[i, j] # flip spin
                array[i, j] = newSpin"""

def plot(array):
	
		x = indices((L, L))[0,:,:]
		y = indices((L, L))[1,:,:]
		color = []
		for i in range(L):
			for j in range(L):
				if array[i, j] == 1:
					color.append([0.0, 0.0, 1.0])
				else:
					color.append([1.0, 1.0, 1.0])
		scatter(x.ravel(), y.ravel(), s=30.0, c=color, edgecolors='none')



"""for i in range(15):
    if i == 0:
        #figure(0)
        #plot(LetterA)
        
        figure(1)
        plot(DamagedA)
        
    monteCarloStep(DamagedA)
    
    if i == 1:
        figure(2)
        plot(DamagedA)
        #print_config(Configuration)
    if i == 2:
        figure(3)
        plot(DamagedA)
        #print_config(Configuration)
    if i == 3:
        figure(4)
        plot(DamagedA)
    if i == 5:
        figure(5)
        plot(DamagedA)"""
    
plot(LetterA)        
show()