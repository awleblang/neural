#!/usr/bin/env python

# weave can be used if chosen in the "steps" method. The "raster" method uses weave and go throughs the entire lattice site by site without making random selections of spins
# in the C code the variable L1 is needed to avoid problems with negative numbers and the modulo operator; numpy avoids this because a[-1] returns the last element of array a

import numpy 
from numpy import *
from pylab import *  
from scipy import weave
from scipy.weave import converters


class Ising2D (object):

	"""Class that describes equilibrium statistical mechanics of the two-dimensional Ising model"""

	def __init__(self, L=32, temperature=10.0):
	
		#numpy.random.seed(222) using this line will yield the same set of random numbers the first time random is called (after that it self seeds)
		
		self.L = L # lattice dimension
		self.N = L**2 # number of sites
		
		self.temperature = temperature
		
		self.w = zeros(9) # store Boltzmann weights
		self.w[8] = exp(-8.0/self.temperature)  # helpful weights when computing dE
		self.w[4] = exp(-4.0/self.temperature)
		
		self.state = ones((self.L, self.L), int) # initially all spins up
		self.energy = - 2 * self.N  # energy of all spins up (each spin has four neighbors but we shouldn't overcount the pairs, i.e., divide by 2)
		self.magnetization = self.N  # total magnetization (not per spin) of all spins up
		
		self.reset()
		
		
	def reset(self):
	
		self.monteCarloSteps = 0
		self.acceptedMoves = 0
		self.energyArray = array([], int)
		self.magnetizationArray = array([], int)
		
		
	def monteCarloStep(self):  # nonweave version
	
		N = self.N
		L = self.L
		w = self.w
		
		state = self.state
		acceptedMoves = self.acceptedMoves
		energy = self.energy
		magnetization = self.magnetization

		
		randomPositions = L * numpy.random.random(2*N)  # to select site at random; this produces an array of 2N random numbers (index lattice sites with i,j) each in range [0,L)
		randomArray = numpy.random.random(N)    # random number for Metropolis algorithm in range [0,1)
		
		for k in range(N): # apply Metropolis method
		
			i = int(randomPositions[2*k])  # choose site at random, int returns integer portion; i will take on random INTEGER values in the range [0,L)
			j = int(randomPositions[2*k+1]) # j will take on random INTEGER values in the range [0,L)
			
			dE = 2*state[i, j] * (state[(i+1)%L, j] + state[i-1, j] + state[i, (j+1)%L] + state[i, j-1])  # modulo operator % incorporates periodic boundary conditions; note that in numpy a[-1]
																										  # automatically loops around to the last element of the array, i.e. periodic BC
			
			if dE <= 0 or w[dE] > randomArray[k]:  # accept the spin flip otherwise return to the k loop
				acceptedMoves += 1
				newSpin = -state[i, j] # flip spin
				state[i, j] = newSpin
				energy += dE   # update the energy to incorporate the flipped spin
				magnetization += 2*newSpin  # update the magnetization
			
		self.state = state
		self.acceptedMoves = acceptedMoves
		self.energy = energy
		self.magnetization = magnetization
		
		self.energyArray = append(self.energyArray, self.energy)
		self.magnetizationArray = append(self.magnetizationArray, self.magnetization)
		self.monteCarloSteps += 1
		
		
		
	def weaveMonteCarloStep(self):
	
		N = self.N
		L = self.L
		w = self.w
		
		state = self.state
		acceptedMoves = array([self.acceptedMoves], int)
		energy = array([self.energy], int)
		magnetization = array([self.magnetization], int)

		randomPositions = L * numpy.random.random(2*N)  # to select site at random
		randomArray = numpy.random.random(N)  # random number for Metropolis algorithm
		
				
		code = """
		int L1 = L-1;
		for (int k = 0; k < N; k++) {
		
			int i = int(randomPositions(2*k));
			int j = int(randomPositions(2*k+1));
				
			int dE = 2*state(i, j) * (state((i+1)%L, j) + state((i+L1)%L, j) + state(i, (j+1)%L) + state(i, (j+L1)%L));
				
			if (dE <= 0 || w(abs(dE)) > randomArray(k)) {
				acceptedMoves(0) += 1;
				int newSpin = -state(i, j);
				state(i, j) = newSpin;
				energy(0) += dE;
				magnetization(0) += 2*newSpin;
			}
		}
		"""
				
		weave.inline(code, ['N', 'randomPositions', 'state', 'L', 'w', 'randomArray', 'acceptedMoves', 'energy', 'magnetization'], 
		type_converters=converters.blitz, compiler='gcc')

		
		self.state = state
		self.acceptedMoves = acceptedMoves[0]
		self.energy = energy[0]
		self.magnetization = magnetization[0]
		
		self.energyArray = append(self.energyArray, self.energy)
		self.magnetizationArray = append(self.magnetizationArray, self.magnetization)
		self.monteCarloSteps += 1


	def rasterMonteCarloStep(self):  # go through sites one by one flipping spins, i.e. no random selection of sites
	
		N = self.N
		L = self.L
		w = self.w
		
		state = self.state
		acceptedMoves = array([self.acceptedMoves], int)
		energy = array([self.energy], int)
		magnetization = array([self.magnetization], int)

		randomArray = numpy.random.random(N)  # random number for Metropolis algorithm
				
		code = """
		int L1 = L-1;
		for (int i = 0; i < L; i++) {
			for (int j = 0; j < L; j++) {
		
				int dE = 2*state(i, j) * (state((i+1)%L, j) + state((i+L1)%L, j) + state(i, (j+1)%L) + state(i, (j+L1)%L));
				
				if (dE <= 0 || w(abs(dE)) > randomArray(i*L+j)) {
					acceptedMoves(0) += 1;
					int newSpin = -state(i, j);
					state(i, j) = newSpin;
					energy(0) += dE;
					magnetization(0) += 2*newSpin;
				}
			}
		}
		"""
				
		weave.inline(code, ['state', 'L', 'w', 'randomArray', 'acceptedMoves', 'energy', 'magnetization'], 
		type_converters=converters.blitz, compiler='gcc')

		
		self.state = state
		self.acceptedMoves = acceptedMoves[0]
		self.energy = energy[0]
		self.magnetization = magnetization[0]
		
		self.energyArray = append(self.energyArray, self.energy)
		self.magnetizationArray = append(self.magnetizationArray, self.magnetization)
		self.monteCarloSteps += 1


	def steps(self, number = 100):  # number = number of MC steps (pass thru entire lattice)
		for i in range(number):
			#self.monteCarloStep()  # no weave; random selection of site
			#self.weaveMonteCarloStep()  # weave with random selection
			self.rasterMonteCarloStep()  # weave going through all lattice sites in order
			
	# Observables
	def meanEnergy(self):
		return self.energyArray.mean() / self.N

	def specificHeat(self):
		return (self.energyArray.std() / self.temperature)**2 / self.N
		
	def meanMagnetization(self):
		return self.magnetizationArray.mean() / self.N

	def susceptibility(self):
		return (self.magnetizationArray.std())**2 / (self.temperature * self.N)
		
	def observables(self):
		print "\nTemperature = ", self.temperature
		print "Mean Energy = ", self.meanEnergy()
		print "Mean Magnetization per spin= ", self.meanMagnetization()
		print "Specific Heat = ", self.specificHeat()
		print "Susceptibility = ", self.susceptibility()
		print "Monte Carlo Steps = ", self.monteCarloSteps, " Accepted Moves = ", self.acceptedMoves

			
	# Visual snapshot of state
	def plot(self):
	
		x = indices((self.L, self.L))[0,:,:]
		y = indices((self.L, self.L))[1,:,:]
		color = []
		for i in range(self.L):
			for j in range(self.L):
				if self.state[i, j] == 1:
					color.append([1.0, 0.0, 0.0])
				else:
					color.append([0.0, 0.0, 1.0])
		scatter(x.ravel(), y.ravel(), s=30.0, c=color, edgecolors='none')

			
		
model = Ising2D(temperature=2.3, L=32)
figure(1)
title ('initial configuration')
model.plot() # initial configuration

model.steps(number=10000)
model.reset()

model.steps(number=10000)
model.observables()
figure(2)
title ('10000 steps after reset')
model.plot()

model.steps(number=10000)
model.observables()
figure(3)
title ('20000 steps after reset')
model.plot()


show()


		