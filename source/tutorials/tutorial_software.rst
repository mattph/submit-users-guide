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


High-Level Questions
~~~~~~~~~~~~~~~~~~~~~~~

* Are you installing software for yourself or your research group?
* Will you want to access the software via JupyterHub?

* How many processors 



* The `Modern Fortran extension <https://marketplace.visualstudio.com/items?itemName=fortran-lang.linter-gfortran>`_ for VSCode (This requires and will automatically install the `C/C++ extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools>`_ as well)

