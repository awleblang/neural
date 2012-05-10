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

L = len(LetterA[0])
N = L**2

def print_config(config):
    for i in range(L):
        for j in range(L):
            if (config[i, j] == -1):
                print('+'),
            else:
                print(' '),
        print('')

def damage(n, damaged):
    for i in range(n):
        damaged[int(L*numpy.random.random(1)), int(L*numpy.random.random(1))] *= -1

damage(50, DamagedA)
#print_config(LetterA)
#print_config(DamagedA)



Jarray = zeros((L, L, L, L))
for i in range(L):
    for j in range(L):
        for k in range(L):
            for l in range(L):
                Jarray[i, j, k, l] = LetterA[i, j]*LetterA[k, l]

RandomConfiguration = numpy.random.random([L, L])
for i in range(L):
    for j in range(L):
        if RandomConfiguration[i, j] < .5:
                RandomConfiguration[i, j] = -1
        else:
                RandomConfiguration[i, j] = 1

def monteCarloStep(array):  # nonweave version
	

    randomArray = numpy.random.random([L, L, L, L])  # random number for Metropolis algorithm

    for i in range(L):
        for j in range(L):
            dE = 0
            for k in range(L):
                for l in range(L):
                    dE += 2*Jarray[i, j, k, l]*array[i, j]*array[k, l]
                                
            if dE < 0: #or exp(-dE/1.0) > randomArray[i, j, k, l])
                array[i, j] *= -1
                                
                                

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



for i in range(100):
    if i == 0:
        figure(0)
        plot(DamagedA)
        
        figure(4)
        plot(LetterA)
    monteCarloStep(DamagedA)
    if i == 0:
        figure(1)
        plot(DamagedA)
        #print_config(Configuration)    
    if i == 1:
        figure(2)
        plot(DamagedA)
        #print_config(Configuration)
    if i == 50:
        figure(3)
        plot(DamagedA)
        #print_config(Configuration)
show()

    