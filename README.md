
Metropolis importance sampling Monte Carlo scheme:
(1) Choose an initial state. 
(2) Choose a site $i$. 
(3) Calculate the energy change $E$ which results if the spin at site $i$ is overturned. 
(4) Generate a random number $r$ such that 0 < $r$ < 1. 
(5) If $r<exp(\Delta E/k_BT)$, flip the spin. 
(6) Go to the next site and go to (3).
