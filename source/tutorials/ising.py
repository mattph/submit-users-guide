import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Example script.')

# Add arguments
parser.add_argument('--temperature', type=float, help='Temperature')
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
import os

def run_mcmc(temperature, J, B, nspins, nsteps):
    ''' This is where the actual Monte Carlo simulation would go.
        Important: this function MUST save all relevant simulation result to file(s)
        (Please see dicussion in text)
    '''
    # We leave the actual construction of this function as an exercise for the student ;)
    print(f"Simulating Ising model w/ temperature {temperature}, J: {J}, B: {B}, length {nspins} spins, {nsteps} Monte Carlo steps.")
    return

# MAIN part of the script for a particular study
# Constants (for this study ... in a different study, we may loop over these)
nsteps = 1000
nspins = 100
J = 10

# get the current directory (will change directories for each simulation)
main_directory = os.getcwd()

# Loop over some parameters to make plots later
simulation_enum = 0  # This is a unique (integer) identifier for each simulation
for temperature in np.arange(50, 301, 50):
    for B in np.arange(5, 10, 5):
        # Update the simulation number
        simulation_enum += 1

        # Print what we're doing on the screen (not necessary)
        print(f"Running simulation # {simulation_enum}: temperature={temperature}, B={B}")

        # Make a unique directory for this set of parameters (aka "for this simulation")
        directory_name = f"simulation_{simulation_enum}"
        os.mkdir(directory_name)
        os.chdir(directory_name)

        # Now run the simulation itself
        run_mcmc(temperature, J, B, nspins, nsteps)

        # Change back to the main directory
        os.chdir(main_directory)

# Here you would read the results of the above simulation and make plots from them.
