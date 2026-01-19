import numpy as np
import random
import matplotlib.pyplot as plt
import time


T = float(input('temperature? ='))
k = 1
L = 20
J = 1
N_steps = 1000


spins = np.random.choice([-1, 1], size=(L, L))

plt.ion()  # Turn on interactive plotting
fig, ax = plt.subplots()
img = ax.imshow(spins, cmap='coolwarm', interpolation='bilinear')
ax.set_title("Ising Model Simulation")

for step in range(N_steps):
    for i in range(L):
        for j in range(L):
            deltaE = 2 * J * spins[i, j] * (
                spins[(i+1)%L, j] + spins[(i-1)%L, j] +
                spins[i, (j+1)%L] + spins[i, (j-1)%L]
            )
            r = random.uniform(0, 1)
            prob = np.exp(-deltaE / (k * T))
            if r < prob:
                spins[i, j] *= -1


    img.set_data(spins)
    ax.set_title(f"Step {step+1}")
    plt.draw()
    plt.pause(0.05)   

plt.ioff()


