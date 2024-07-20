import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Example script.')

# Add arguments
parser.add_argument('--temperature', type=float, help='Temperature value')
parser.add_argument('--J', type=float, help='Spin-spin interaction strength')  # Added J parameter here
parser.add_argument('--B', type=float, help='External magnetic field strength')
parser.add_argument('--nspins', type=int, help='# Spins in the chain')
parser.add_argument('--nsteps', type=int, help='Number of Monte Carlo steps')

# Parse arguments
args = parser.parse_args()

# Use the arguments
print(f"Temperature: {args.temperature}, J: {args.J}, B: {args.B}, # Spins: {args.nspins}, # Monte Carlo Steps: {args.nsteps}")




# original code:

import numpy as np

def run_mcmc(temperature, J, B, nspins, nsteps):
    '''This is where the actual Monte Carlo simulation would go.'''
    # We leave the actual construction of this function as an exercise for the student ;)
    print(f"Simulating Ising model with temperature {temperature}, J: {J}, B: {B}, length {nspins} spins, {nsteps} Monte Carlo steps.")
    return

# Main part of the script.  Here we loop over different values
# Constants (for this study)
nsteps = 1000
nspins = 100
J = 10

# Loop over other parameters to make plots later
for temperature in np.arange(50, 301, 50):
    for B in np.arange(50, 301, 50):
        run_mcmc(temperature, J, B, nspins, nsteps)

# Here you would read the results of the above simulation and make plots from them.
