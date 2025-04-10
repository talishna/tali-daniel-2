#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:56:35 2023

@author: Talisha
"""

# Check if there are external arguments given to main,
import sys
if len(sys.argv) >= 2:
    HPC = True  # run with external parameters
else:
    HPC = False # run with main parameters
import os
if HPC: # set cores to 1 , MUST BE BEFORE IMPORTING NUMPY!
    os.environ['OMP_NUM_THREADS'] = '1'
    os.environ['MKL_NUM_THREADS'] = '1'
else:
    # clear console screen
    #clear = lambda: os.system('clear')
    #clear()
    x=1
from parameters import parameters
def main():
    if HPC:
        # directory
        project = str(sys.argv[1])

        # static parameters
        spar = parameters()
        spar.add("NSitesk",int(sys.argv[2]))
        spar.add("NSitesC",int(sys.argv[3]))
        spar.add("m",int(sys.argv[4]))
        spar.add("mu",float(sys.argv[5]))
        spar.add("Sweeps",int(sys.argv[6]))
        spar.add("Uk",float(sys.argv[7]))
        spar.add("UCk",float(sys.argv[8]))
        spar.add("tu",float(sys.argv[9]))
        spar.add("td",float(sys.argv[10]))
        spar.add("t",float(sys.argv[11]))
        spar.add("Ed",float(sys.argv[12]))
        spar.add("B",float(sys.argv[13]))
        spar.add("Lambdak",float(sys.argv[14]))
        spar.add("LambdaC",float(sys.argv[15]))

        # dynamic parameters
        dpar = parameters()
        dpar.add("V",float(sys.argv[16]))
        dpar.add("dt",float(sys.argv[17]))
        dpar.add("time_steps",int(sys.argv[18]))
        dpar.add("ST_order",int(sys.argv[19]))

    else:
        # directory
        project = "Cshape-kondo"

        # static parameters
        spar = parameters()
        spar.add("NSitesk", 16) # spinfull Lead
        spar.add("NSitesC", 15) # spinless C-shape Lead
        spar.add("m", 64)

        spar.add("mu", 0)
        spar.add("Sweeps", 5)
        spar.add("Uk", 2)       # Impurity interaction
        spar.add("UCk", 1)       # Impurity -C-shape lead interaction
        spar.add("tu", 1)
        spar.add("td", 1)
        spar.add("t", 0.5)
        spar.add("Ed", -1)
        spar.add("B", 0)
        spar.add("Lambdak", 1.6)
        spar.add("LambdaC", 1)
        # dynamic parameters
        dpar = parameters()
        dpar.add("V", 0.01)
        dpar.add("dt", 0.02)
        dpar.add("time_steps", 800)
        dpar.add("ST_order", 2)

    # directory
    if not os.path.isdir('./DATA'):
        os.mkdir('./DATA')

    if not os.path.isdir('./DATA/' + project ):
        os.mkdir('./DATA/' + project )