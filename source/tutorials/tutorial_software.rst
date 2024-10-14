Tutorial: Getting Started - Choosing Where to Run your Jobs & How to Install/Manage Your Software
--------------------------------------------------------------------------------------------------

.. warning::

    Note to subMIT Team:  The highlighted "warnings" below are actually notes to the team (todo items) and should be addressed and removed *before publishing.*

On subMIT, we provide access to a number of different advanced computing resources including not only HPC-style resources managed by SLURM, but also High-Throughput sytle resources managed by HTCondor.
We also like to put you in control of managing your software, so this results in a number of options available to you as to how to install and manage your software.
This tutorial guides you through deciding which options best fit *your* needs.

.. |ShowMore| replace:: More Detail (click here to show/hide)

.. tip:: 
    Click on the boxes throughout this tutorial labeled "|ShowMore|" in order to see more detailed information and/or helpful hints.  Click again to hide the info again.

.. admonition:: |ShowMore|
    :class: dropdown

    .. The instructions below make use of the menus to run commands, but you could alternatively run the commands using keyboard shortcuts, or by pulling up the Command Palette (Command+Shift+P on Mac, or Ctrl+Shift+P on Windows or Linux) and simply typing the command (e.g. Command+Shift+P then type "connect to host").

    .. tip:: 
    
        Click any picture to enlarge it.  (Then use your browser's 'Back' button to return to the tutorial).

You will learn ...
~~~~~~~~~~~~~~~~~~~~~

* How to choose between the various computing resources available via subMIT
* How to choose between options for installing/managing software for individual users or research groups
* Differences in software management requirements for HTCondor vs SLURM and heavy vs light simultaneous access


.. Definitions
.. ~~~~~~~~~~~

.. Nuances in terminology in this field can often vary in different contexts, so we define how we will use a few terms in this tutorial.

.. * Batch job = A set of tasks which run without input/intervention from the user.  These are managed by a script submitted to a scheduler and often launch at a later time.
.. * High Throughput style Computing = A workflow of many jobs which run indepenently from one another (no communication between jobs)
.. * High Performance style Computing = 


Step 1: Choose where your jobs will run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

    Maybe present this information different ways: flow chart, table, etc.  Different people prefer different presentations of information.

Here is a summary table comparing resources managed by HTCondor vs SLURM

.. .. |  | HTCondor | SLURM |
.. .. |--|----------|-------|
.. .. | # available compute resources | Largest | Large |
.. .. | supports modest[2]_ intra-node information sharing (MPI or multi-threading)[1]_ | Yes | Yes |
.. .. | supports large[2]_ intra-node information sharing (MPI or multi-threading)[1]_ | No | Yes |
.. .. | supports inter-node information sharing (MPI) | No | Yes |
.. .. | has persistent disk storage | No | Yes | 
.. .. | direct access to shared network drives `/home`, `/work`, `/ceph` | No | Yes |
.. .. | supports containers | Yes | Yes |
.. .. | can run software installed in `/work` | No | Yes |

+------------------------------------------------------------------------------------------------+----------+--------+
|                                                                                                | HTCondor | SLURM  |
+================================================================================================+==========+========+
| # available compute resources                                                                  | Largest  | Medium |
+------------------------------------------------------------------------------------------------+----------+--------+
| supports modest [#htmt]_ intra-node information sharing (MPI or multi-threading) [#intranode]_ | Yes      | Yes    |
+------------------------------------------------------------------------------------------------+----------+--------+
| supports large [#htmt]_ intra-node information sharing (MPI or multi-threading) [#intranode]_  | No       | Yes    |
+------------------------------------------------------------------------------------------------+----------+--------+
| supports inter-node information sharing (MPI)                                                  | No       | Yes    |
+------------------------------------------------------------------------------------------------+----------+--------+
| has persistent disk storage                                                                    | No       | Yes    |
+------------------------------------------------------------------------------------------------+----------+--------+
| direct access to shared network drives `/home`, `/work`, `/ceph`                               | No       | Yes    |
+------------------------------------------------------------------------------------------------+----------+--------+
| supports containers                                                                            | Yes      | Yes    |
+------------------------------------------------------------------------------------------------+----------+--------+
| can run software installed in `/work`                                                          | No       | Yes    |
+------------------------------------------------------------------------------------------------+----------+--------+
| can run software installed in `/cvmfs`                                                         |          | Yes    |
+------------------------------------------------------------------------------------------------+----------+--------+

.. warning::

    Where does `/cvmfs` fit into this?  Is that accessible on HTCondor manged resources? 



If you prefer the same information presented as a decision-process, please see:

* Can each cpu processor in my workflow operate *independently*, or is significant information-sharing between processors required during run time?  

  * If all cpu's may operate independently, then you may run on *either* HTCondor or SLURM managed resources.  (This is typically called a "High Throuput workflow")

  * If information-sharing is required, does information need to be shared across nodes (e.g. inter-node communication via MPI)?

    * If you require inter-node communication (e.g. via MPI), then you must run on a SLURM managed resource.

    * If you only share information within a single node [#intranode]_, do you require a large or small number of processors per job?

      * HTCondor resources can accomodate a modest number of processors per job [#htmt]_

      * SLURM resources can accomodate small through large number of processors in a single job.

If your workflow may fit on either HTCondor or SLURM resources, then a few tradeoffs to keep in mind are: HTCondor provides access to a larger pool of resources, but software *must* be packaged in containers, and data must be transferred on & off of the resource *at job run time* (there are no mounted peristent storage drives on HTCondor resources).  SLURM resources have direct access to your `/home, /work/, & /ceph` directories, so they can access software & data located on those spaces (and can save output directly to those spaces).  In addition SLURM *can* run software via containers.

.. [#intranode] This can be done via message-passing (e.g. MPI, distributed memory, "communication") *or* multi-threading (shared memory).

.. [#htmt] HTCondor resources can accomodate a modest number of processors per job.  To check if your job can fit on a HTCondor resource, check here: ******

.. warning::

    Fill in the **** above for how to check the # of processors allowed within a single HTCondor job 

.. warning::

    You CAN run an application in HTCondor which uses MPI within a single node, correct?  You can just put MPI in your container, right?  Or does this require MPI to be installed outside the container as well?  If not, then the above decision needs to be corrected.


Step 2: Choose software installation/management and location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTCondor Resources
------------------

If you are using HTCondor, you must use containers to manage your software.  Please see more information here: :ref:`containers`

.. warning::

    Is this accurate?  Can you alternatively access e.g. a conda environment placed into `/cvmfs`?


If instead, you will use SLURM managed resources, you have further decisions to make as to how you will install your software and where you will place it.



.. _how-install-slurm:

SLURM Resources: How to install/manage your software
-------------------------------------------------------------

On a SLURM manged resource connected to subMIT, you can either:

* Use containers to install/manage your software :ref:`containers`

OR 

* Perform a traditional installation on a shared drive (`/work`, `/cvmfs`)


To do the latter, you can either install software manually (e.g. compiling custom code from source) or use a package and/or environment manager such as `conda` or `spack`.  If using the latter, you can use the `environment management <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_ feature to separate different installations for different groups etc.  Please see `the software page <https://submit.mit.edu/submit-users-guide/program.html>`_ of our users guide for more information.


You must also decide *where* to place your software: :ref:`where-to-put`



.. _where-to-put:

SLURM Resources: WHERE to place your software
------------------------------------------------------

* Will there be large [#largecvmfs]_ simultaneous access to this software installation?

  * If yes, you should place it on `/cvmfs` :ref:`cvmfs-howto` *instead* of `/work`

  * Otherwise, you may place it in your `/work` space.

You must also decide how to install/manage your software: :ref:`how-install-slurm`




.. _group-vs-individual:

What do do if you are installing software for your entire group?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* These instructions work for individual or groups, since directories are public by default on subMIT.
  
* You will need to provide the full path to your group members for them to access your software

  * If you are using conda environments in your `/work`, running `conda env list` will display the full path on the right hand side.  Your group members will have to paste that full path into their `conda activate` or `conda run` commands.  E.g. `conda activae [full path to your work env]`.

* Keep in mind to consider the *total* amount of simultaneous access you expect (sum over all access by all group members) :ref:`where-to-put`

* *If* you prefer to have each group member have their own individual copy of your conda environment, please see the `conda documentation <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment>`_ for sharing environments using the `conda export` command.  Note: any changes made to environments will *not* be automatically synced across users with this method.









.. _cvmfs-howto:

Installing your software on the `/cvmfs` space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warnings::

    Need to write this section!!!  plus answer questions:

    CVMFS Questions:
    
    * How do users easily update this when they, for instance, make code & version changes?  Is this not good for a development environment?
  
    * Can groups add their non-conda and non-container self-installed software to `/cvmvs`?  If so, how?  (E.g. compile c++ application from source code.)
    
    * How does group access to this work?  Is it just public?


.. [#largecvmfs] If you expect more than roughly **** jobs total (across all users) to be using this software simultaneously, you should have your software placed on `/cvmfs`.

.. warnings::

    Can we put a number (ballpark, rule of thumb) on what counts as "large" simultaneous access for a software dir?  I.e. when is it OK to be in `/work` vs when should it be in `/cvmfs`?



.. _containers:

Containers
~~~~~~~~~~

.. warnings::

    Need to write this or link to an external resource
    

