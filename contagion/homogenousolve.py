import matplotlib.pyplot as plt
import numpy as np


#%% solve R given n,T

def find_R(n,T):
    if n*T <= 1:
        return 0
    
    guess = 0.5
    
    while True:
        #print(guess)
        newGuess = 1-(1-guess*T)**n
        if abs(newGuess - guess) < 0.000001:
            return newGuess
        else:
            guess = newGuess
 

#%% probability of infection

def p(n,T,R):
    return 1-(1-R*T)**n           

#%% define utility

def inverse_U(n):
    if n==0:
        return -2
    return -1/n -n/200

def linsquare_U(n):
    return 20*n - n**2

U = linsquare_U

#%% solve for equilbrium

c = 30 # cost of catching disease 0.08
T = 0.3 # transmission chance per connection.
maxConnections = 20
minConnections = 0#int(1/T)+1 #need to ignore the n's below which no outbreak occurs.
grid = np.linspace(minConnections,maxConnections,maxConnections-minConnections+1)# set of connection numbers to iterate over
#grid = range(101)
utils = [U(n)-c*p(n,T,find_R(n,T)) for n in grid]

plt.plot(grid,utils)
plt.show()

maxUtil = max(utils)
bestConnections = utils.index(maxUtil)+minConnections
equilibriumR = find_R(bestConnections,T)
print("max=",maxUtil,"; argmax=",bestConnections, "; R=",find_R(bestConnections,T))















