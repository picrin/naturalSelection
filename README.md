# The effect of natural selection on relatedness of individuals in randomly mating population.

This is a 4th year project developed as a part of Joint Honours Computer Science and Mathematics degree at University of Glasgow. The project is worth 20 credits.

The dissertation can be found in `dissertation/l4proj.pdf`

The framework can be found in `naturalSelection`

# Installation and Usage

The naturalSelection framework is distributed in source form as a standard python module, and can be used and handled in the way any python module can, in particular `import naturalSelection` should work as expected.

In addition I'm including the `project` bash script, which has the purpose of running test cases to assure compliance with Cpython 2 and Cpython 3, as well as the execution of the particular experiment implemented using this framework.

To access framework's manual, make sure your working directory contains the `naturalSelection` directory and type `pydoc`

In order to run a simulation batch and create all the graph files, compute Tmrca and run Mann-Whitney statistics you can execute `./project --runExperiments s2 mrca2 proc2`. Be warned, it takes ~ 2 hours on modern commodity hardware. The graphs will be generated and written in `results` directory. The step s2 does not have any dependencies required apart from Cpython 2.7, Cpython 3, pypi or jython. proc2 is dependent on the networkx package.

To carry out some symbolic derivation of mathematical formulae used in this project you can execute `./project --derive`. This step has a dependency on the sage package, which can be installed, e.g. on modern Fedora by executing `dnf install sagemath` as root user. This dependency is optional and restricted to this particular command so as not to force any user to install sage as dependency in their system.

To unit test, execute `./project --test`.

You can install all of dependencies described above using virtualenv in the following way:
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

This should install all required dependencies for python 2 (a.k.a. Cpython 2). Installing networkx for python 3 through pip seems to be broken. For python 3 I found necessary to install dependencies using my distribution's package manager.
