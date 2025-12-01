import random
import numpy as np
import matplotlib.pyplot as plt
c=0
T=2.7
k=1
L=10
N_steps=int(input('no. of steps= '))
J=1 #assuming for simmpliciity
spins=np.random.choice([-1, 1], size=(L, L))
M_list=[]
E_list=[]

for step in range(N_steps):
    E=0
    
    #print("spins of lattice structure:")
    #print(spins)


    for i in range(L):
        for j in range(L):
            deltaE = 2 * J * spins[i, j] * (
                spins[(i+1)%L, j] + spins[(i-1)%L, j] + 
                spins[i, (j+1)%L] + spins[i, (j-1)%L]
            )
            r = random.uniform(0, 1)

            prob=np.exp(-deltaE/(k*T))
            if r<prob:
                spins[i, j] *= -1
    for i in range(L):
        for j in range(L):
            E -= J * spins[i,j] * (spins[(i+1)%L, j] + spins[i, (j+1)%L])


    #print("the spins of new lattice structure:")
    #print(spins)

    M = np.sum(spins) / (L*L)
    #print("Magnetization per spin:", M)

    E_per_spin = E / (L * L)

    M_list.append(M)
    E_list.append(E_per_spin)


t_list = list(range(len(M_list)))
plt.plot(t_list, M_list, color='blue')
plt.xlabel('t')
plt.ylabel('M')
plt.yticks([-1, 0, 1])
plt.show()
    