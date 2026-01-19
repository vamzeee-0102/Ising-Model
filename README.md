The energy of a lattice is calculated using the following formula:

$E = J \sum_{\langle ij \rangle} s_i s_j$

**Metropolis importance sampling Monte Carlo scheme**:

(1) Choose an initial state. 

(2) Choose a site $i$. 

(3) Calculate the energy change $E$ which results if the spin at site $i$ is overturned. 

(4) Generate a random number $r$ such that 0 < $r$ < 1. 

(5) If $r<exp(\Delta E/k_BT)$, flip the spin. 

(6) Go to the next site and go to (3).

Since simulations are performed on finite systems, one important question which arises is how to treat the ‘edges’ or boundaries of the lattice. These boundaries can be effectively eliminated by wrapping the d-dimensional lattice on a (d + 1)-dimensional torus. This boundary condition is termed a ‘periodic boundary condition’ (pbc) so that the first spin in a row ‘sees’ the last spin in the row as a nearest neighbor and vice versa. The same is true for spins at the top and bottom of a column.

~From "A Guide to Monte Carlo Simulations in Statistical Physics" by D.P. Landau, Kurt Binder
