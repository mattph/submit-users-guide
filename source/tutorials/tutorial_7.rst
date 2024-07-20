.. raw:: html

    <style> 
        .red {color:red;} 
        .black {color:black; text-shadow:none;} 
        .gold {color:#fecb2f;}
    </style>

.. role:: red

.. role:: black

.. role:: gold

Tutorial 7: Basic Intro to Running Your Code in Parallel
--------------------------------------------------------

.. |ShowMore| replace:: More Detail (click here to show/hide)

.. tip:: 
    Click on the boxes throughout this tutorial labeled "|ShowMore|" in order to see more detailed information and/or helpful hints.  Click again to hide the info again.

.. admonition:: |ShowMore|
    :class: dropdown

    This is an example of a "|ShowMore|" box.  Ordinarily this would contain additional information.
    
You will learn to ...
~~~~~~~~~~~~~~~~~~~~~

* ______
 
  .. todo: fill this out

.. admonition:: Note

    Even though this tutorial uses Python as an example, most of these techniques are general and *not* restricted to Python. If you have *any* code that can be run from the command line, you can likely run it in parallel using these techniques.  Please see also `the section discussing bash loops <_bash-loop>`_.

Scope of this tutorial
~~~~~~~~~~~~~~~~~~~~~~

This tutorial is intended to be a very basic introduction to running your code in parallel.  we will not cover advanced techniques, but hopefully this will serve as a starting point and get you up and running your existing code quickly.  This is intended to be a first step in your journey.

Introduction
~~~~~~~~~~~~

Please see our additional pages on introduction to HPC and parallel computing before starting this tutorial.  This tutorial is the nuts and bolts of how to execute those concepts in a simple introductory way.

.. todo: make this other page (see my earlier IAP talk)

The example
~~~~~~~~~~~

We will be looking at a simple 1D Ising model with first nearest-neighbors interactions.
This is often treated using Monte Carlo methods, particularly the Metropolis algorithm.
Let's say we have a python script that simulates the system for a given set of parameters: `temperature`, `J` (spin-spin interaction strength), `B` (external field strength), `nspins` (length of the chain), `nsteps` (number of Monte Carlo steps), etc.
Please see the example function at the bottom of the page (the contents are not very important here).
.. the example is in ising.py in this same directory

Let's say that within your code, you have a function, `run_mcmc`, which does the MC simulation for a given set of parameters.

.. code-block:: python

    def run_mcmc(temperature, J, B, nspins, nsteps):
        ''' This is where the actual Monte Carlo simulation would go.
            Important: this function MUST save all relevant simulation result to file(s)
            (Please see dicussion in text)
        '''
        # We leave the actual construction of this function as an exercise for the student ;)
        print(f"Simulating Ising model with temperature {temperature}, J: {J}, B: {B}, length {nspins} spins, {nsteps} Monte Carlo steps.")
        return

.. admonition:: Important

    We assume the function `run_mcmc` saves all relevant results of the simulation to a file(s).  
    (In other words, not just returned in memory).
    If that is not the case you will need to modify the function (or wrap it in another function) to save the results to a file.

    It is also crucial that these simulation files are either placed in a unique directory for each set of simulation paramters (or the files themselves are named uniqely for each set of parameters).
    This is to 1) prevent overwriting results and 2) prevent parallel simulations from trying to simultaneously write to the same file.
    In the example below, this is accomplished by the python script creating/naming a new unique directory before `run_mcmc` is called.

    .. admonition:: |ShowMore|
        :class: dropdown

        Why?  When we run the function in parallel, each simulation will run indepenently and may run in the same time or in an unpredictable order.  Therefore each simulation must save its own results to be read in and combined later.

Now let's say you are performing a study where you want to plot the magnetization as a function of temperature and applied magnetic field (for a fixed chain length, number of Monte Carlo steps, and spin-spin interaction strength).
To that end, you run the following script which loops over those parameters and calls `run_mcmc` for each set of parameters.

.. todo: better to not have function definition here too?
.. code-block:: python

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

This script performs the calculation serially (each simulation is run one at a time sequentially).
The first step in parallelizing this script is to identify which parts can be run in parallel (independently, in any order, even simultaneously).
In this case, every iteration of this loop, every call of `run_mcmc`, is completely independent (does not depend on previous iterations), so we can run each `run_mcmc` call in parallel.

.. admonition:: Note

    *Especially* when starting with parallel / high-performance computing, it's best to stick to a *modest* number of parallel (simultaneous) tasks.
    Once you verify everything is working as expected, you can slowly scale up as you gain more experience and understand the potential consequences and considerations of scaling up (increasing the number of parallel calculations).

The first step in the methods of this tutorial is to pull `run_mcmc` (the part we want to run in parallel) into a separate script file so that we can call it from the command prompt.  Let's call this script file `single_simulation.py`.
We will need a way to feed the input parametrs into `single_simulation.py`.  Here we will do that via command line arguments, but you could use other methods such as writing `single_simulation.py` to read the inputs from a file. 
.. todo: do I want to do file instead?  Well, let's do it this way and see if any method works better with an input file

If you would like to see `single_simulation.py`, click |ShowMore| below.

.. code-block:: python

    import argparse

    def run_mcmc(temperature, J, B, nspins, nsteps):
        ''' This is where the actual Monte Carlo simulation would go.
            Important: this function MUST save all relevant simulation result to file(s)
            (Please see dicussion in text)
        '''
        # We leave the actual construction of this function as an exercise for the student ;)
        print(f"Simulating Ising model w/ temperature {temperature}, J: {J}, B: {B}, length {nspins} spins, {nsteps} Monte Carlo steps.")
        return

    if __name__ == "__main__":
        # Parse the command line arguments
        parser = argparse.ArgumentParser(description='Run a single simulation of the Ising model.')
        parser.add_argument('--temperature', type=float, help='Temperature of the system.')
        parser.add_argument('--J', type=float, help='Spin-spin interaction strength.')
        parser.add_argument('--B', type=float, help='External magnetic field strength.')
        parser.add_argument('--length', type=int, help='Length of the chain.')
        parser.add_argument('--steps', type=int, help='Number of Monte Carlo steps.')
        args = parser.parse_args()

        # Run the simulation
        run_mcmc(args.temperature, args.J, args.B, args.length, args.steps)

Now you could run this script from the command line with the following command:

.. code-block:: bash

    python single_simulation.py --temperature 300 --J 10 --B 5 --length 100 --steps 1000

This would run a single simulation of the Ising model with temperature 300, J=10, B=5, length 100 spins, and 1000 Monte Carlo steps.

.. _bash-loop:

.. admonition:: Note

    Now we are more clearly treating the general case of parallelizing *any* calculation which is called from the command line, not just a Python script.  Just replace the line above with whatever you would type in the terminal to run an independent simulation.  For example, perhaps you are running a command or script within a loops within a bash script instead of the python loops above.

Now we are ready to move on to parallelizing this.
Click on the tabs below to see the calculation run in parallel using different methods.
In each case, you would gather your results and make your plots *after* all the "jobs" or "tasks" are complete.
Hopefully seeing the same example done multiple ways will help abstract the essence of what's being done.


.. tabs::

   .. group-tab:: :gold:`SLURM Job Arrays`

    SLURM job arrays are great for performing many *similar* jobs in parallel, like parameter sweeps as in this example.
    One could also manually submit each of these as separate SLURM jobs (see our other tutorials on SLURM), but here we will use job arrays since that is better-suited for this type of calculation.
    .. highlight the looping python code and ask AI to do it using slurm job arrays & check results
    .. (Actually run it (FAKE calculation) on the cluster to verify that it works
    .. do the same for snakemake, subprocesses (or whatever it's called), dask, etc (can ask AI for more)
    .. can eventually add a section on just optimizing the code, compiling the code, and GPUs (but that would be different task)
    .. maybe actually add a section for separate slurm jobs just for instructional purposes (say this is like what job arrays are doing - without the benefits)



      .. :black:`Open the Terminal application.`
      .. :black:`This can be done by clicking on Lanuchpad or hitting F4, and then typing "terminal" followed by the Return key.`

   .. group-tab:: :gold:`Windows`

      :black:`We recommend you install & use Windows Subsystem for Linux.  If you do not wish to at this time, you may follow these directions to generate keys natively in Windows...`

      :black:`Click in the Start Menu search bar (next to the Windows icon), then type "command prompt" followed by the Enter key.`


.. admonition:: Important

    Above we mentioned the importance that parallel simulations *not* try to write to the same file simultaneously.
    The same is true for *any* resource which is not designed for multiple simultaneous access.



References & AI Usage
~~~~~~~~~~~~~~~~~~~~~

This tutorial was created with the assistance of generative AI which may include A2rChi, GitHub Copilot, and Google Gemini.
.. Copilot tried to take credit for writing the whole tutorial as I wrote that last line!


.. What if my code already loops over parameter values?
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. In this case, you could modify your code to extract the "guts" of the loop into its own script which can be called as above.
.. An alternative (with no code modification) is to use your code as-is and just pass
.. Here the important thing to do is look at the code and realize which loops can be parallelized and which cannot.
.. For example, loops where one iteration does not depend on the previous iteration can be parallelized.
.. Or sometimes loop interations could be paralelized and combined in a simple way afterwars such as a sum.