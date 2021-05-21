import matplotlib.pyplot as plt
import numpy as np
from scipy.special import lambertw

#%% evaluate possible guesses for R

def grid_search(vrtau,currentBest,gridwidth, gridsize=100):
    '''vrtau is a parameter, 
    currentBest is the center of the grid we check, 
    and gridwidth is the radius around that center we check.
    We need to exclude  zero as a solution. So rather than simply finding the minimum,
    we find the crossover from positive difference to negative difference.
    '''
    mingrid = max(0,currentBest-gridwidth)
    maxgrid = currentBest+gridwidth
    grid = np.linspace(mingrid,maxgrid,gridsize)
        
    for R in grid:
        if R > 1-np.exp(-vrtau*R):
            return R

def iterative_grid_search(vrtau,initialGuess=0.5,numberOfIterations=100):
    '''Checks entire range [0,1], then progressively narrows in on finer and finer optimal segments.'''
    if vrtau <= 1:
        return 0
    else:
        currentGuess = initialGuess
        for iteration in range(numberOfIterations):
            currentWidth = (1/10)**iteration
            currentGuess = grid_search(vrtau,currentGuess,currentWidth)
            #print(currentWidth,currentGuess)
        return currentGuess
    #There's lots of redundant checking here. Could probably speed up a bit by removing some of the overlap.



def solve_with_lambert(vrtau):
    '''This should give the exact solution to R = 1-exp(-vrtau*R).
    If everything went correctly, should give same results as above solver.'''
    return ((lambertw(- np.exp(-vrtau) * vrtau) + vrtau)/vrtau).real


#%% Graph vrtau vs size of epidemic.
    
def plot_epidemic_size():
    X = np.linspace(0,5,1000)
    Y1 = [solve_with_lambert(vrtau) for vrtau in X]
    Y2 = [iterative_grid_search(vrtau) for vrtau in X]

    plt.plot(X,Y1)
    #plt.plot(X,Y2)
    plt.show()

plot_epidemic_size()














#%%


'''    
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



'''











