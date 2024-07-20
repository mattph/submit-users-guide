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




Let's say, to call the function, we run the following command in the terminal:

.. code-block:: bash

   python ising.py --temperature 300 --length 100 --steps 5000

Click on the tabs below to see the calculation run in parallel using different methods.
In each case, once all the "jobs" or "tasks" are complete, we will likely want to combine the results together to plot them.
Hopefully seeing the same example done multiple ways will help abstract the essence of what's being done.


.. tabs::

   .. group-tab:: :gold:`In a bash loop (not parallel)`

    This method is not actually parallel, but we include it for reference as it may clarify the other examples.
    Of course if you are running a python script you would probably 


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