import numpy 
from numpy import *
from pylab import * 

LetterA = array( [ [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, 1, -1, -1, -1],
                   [-1, -1, -1, 1, 1, 1, 1, 1, -1, -1],
                   [-1, -1, -1, -1, 1, 1, -1, 1, 1, -1],
                   [-1, -1, -1, -1, 1, 1, -1, -1, 1, 1],
                   [-1, -1, -1, -1, 1, 1, -1, -1, 1, 1],
                   [-1, -1, -1, -1, 1, 1, -1, 1, 1, -1],
                   [-1, -1, -1, 1, 1, 1, 1, 1, -1, -1],
                   [1, 1, 1, 1, 1, 1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, -1, -1, -1, -1, -1] ])

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

LetterD = array([ [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
                  [1, 1, 1, -1, -1, -1, -1, 1, 1, 1],
                  [-1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
                  [-1, -1, 1, 1, 1, 1, 1, 1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] ])

LetterE = array([ [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
                  [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
                  [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
                  [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
                  [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] ])


"""DamagedA = array( [ [1, 1, -1, 1, 1, -1, 1, -1, -1, -1],
                    [-1, 1, -1, 1, 1, 1, -1, -1, -1, 1],
                    [1, -1, -1, 1, -1, 1, 1, 1, 1, -1],
                    [-1, -1, -1, -1, 1, -1, -1, 1, 1, -1],
                    [1, -1, 1, -1, 1, 1, -1, -1, 1, 1],
                    [1, -1, -1, -1, 1, -1, 1, -1, 1, 1],
                    [-1, -1, 1, -1, -1, 1, -1, -1, -1, -1],
                    [-1, -1, 1, 1, -1, -1, -1, 1, -1, 1],
                    [-1, 1, -1, -1, 1, -1, 1, -1, -1, -1],
                    [-1, 1, 1, 1, -1, 1, 1, -1, -1, -1] ])"""

DamagedA = array( [ [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],
                   [1, 1, 1, 1, 1, 1, 1, -1, -1, -1],
                   [-1, -1, -1, 1, 1, 1, 1, 1, -1, -1],
                   [-1, -1, -1, -1, 1, 1, -1, 1, 1, -1],
                   [-1, -1, -1, -1, 1, 1, -1, -1, 1, 1],
                   [-1, -1, -1, -1, 1, 1, -1, -1, 1, 1],
                   [-1, -1, -1, -1, 1, 1, -1, 1, 1, -1],
                   [-1, -1, -1, 1, 1, 1, 1, 1, -1, -1],
                   [1, 1, 1, 1, 1, 1, 1, -1, -1, -1],
                   [1, 1, 1, 1, 1, -1, -1, -1, -1, -1] ])

ArrayofLetters = array([LetterA, LetterB, LetterC, LetterD])

L = len(LetterA[0])         #dimension of lattice
N = L**2                    #number of neurons in network
M = len(ArrayofLetters)     #number of stored patterns


Jarray = zeros((L, L, L, L))
for m in range(M):
    Letter = ArrayofLetters[m]
    for i in range(L):
        for j in range(L):
            for k in range(L):
                for l in range(L):
                    Jarray[i, j, k, l] += Letter[i, j]*Letter[k, l]
Jarray = (1.0/M)*Jarray

for i in range(9500):
    a = int(L*numpy.random.random(1))
    b = int(L*numpy.random.random(1))
    c = int(L*numpy.random.random(1))
    d = int(L*numpy.random.random(1))
    
    Jarray[a,b,c,d] = 0
    


def damage(n, damaged):
    for i in range(n):
        damaged[int(L*numpy.random.random(1)), int(L*numpy.random.random(1))] *= -1



def monteCarloStep(array):  # nonweave version
	
    randomArray = numpy.random.random([L, L, L, L])  # random number for Metropolis algorithm

    for i in range(L):
        for j in range(L):
            dE = 0
            for k in range(L):
                for l in range(L):
                    dE += 2*Jarray[i, j, k, l]*array[i, j]*array[k, l]
                                
            if ((dE < 0) or (exp(-dE/7.5) > randomArray[i, j, k, l])):
                newSpin = -array[i, j] # flip spin
                array[i, j] = newSpin

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

damage(30, DamagedA)

for i in range(15):
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
        plot(DamagedA)
    
#plot(LetterC)        
show()