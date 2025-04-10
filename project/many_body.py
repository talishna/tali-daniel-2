#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:33:32 2023

@author: Daniel & Tali
"""

from qsystem import qsystem
import numpy as np
from scipy.linalg import expm
from numpy.linalg import eigh
import matplotlib.pyplot as plt
from parameters import parameters
from scipy import linalg as linalg
from scipy import sparse as sparse
import scipy.sparse.linalg as sp_linalg

class many_body(qsystem):

    # initializing the system, with sites= sitesL + 1 + sitesR
    def __init__(self, sites):
        # calls super class and runs it's initintioalization method
        qsystem.__init__(self, sites)
        self.sitesL = int(sites/2)-1
        self.sitesR = int(sites/2)

    def s(matrix, spin_index): # matrix is the matrix I want to do kron prod for. options
        # are: s_z, s_plus, s_minus # spin_index is the spin index inside the chain, so if it's 1 it'll be the 1st spin if 2 the 2nd spin ect.
        M = sparse.kron(sparse.identity(2**(spin_index-1), dtype=complex),
                        sparse.kron(matrix, sparse.identity(2**(self.sites-spin_index), dtype=complex))) # the first identity matrix is of size 2^i the last identity matrix is of size N-i
        return M
#%%

#%%

#%%

#%%
