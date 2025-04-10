#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:36:10 2023

@author: Daniel & Tali
"""



from qsystem import qsystem
import numpy as np 
from scipy.linalg import expm
from numpy.linalg import eigh
import matplotlib.pyplot as plt
from parameters import parameters

class non_interacting(qsystem):

    # initializing the system, with sites= sitesL + 1 + sitesR
    def __init__(self, sites):
        # calls super class and runs it's initintioalization method
        qsystem.__init__(self, sites)
        self.sitesL = int(sites/2)-1
        self.sitesR = int(sites/2)
        
        
    # construct the voltage bias 
    def V(self,v):
        L = np.append(np.full(self.sitesL,1),np.full(self.sitesR+1,0))
        R = np.append(np.full(self.sitesL+1,0),np.full(self.sitesR,-1))
        V = v/2*(np.diag(L) + np.diag(R))
        return V

    # define the Hamiltonian for time t<=0, save spectrum, tunneling_array, U_dag
    def h0(self,mu, t, tp, Ed): # martix of the coefficients of the hamiltonian for time<0
        
        # construct the tunneling array amplitudes, NOTE: only real values are considered
        self.tunneling_array = np.hstack((np.full(self.sitesL-1, t),np.full(2,tp),np.full(self.sitesR-1, t)))
        
        # construct the on-site energy array
        muArr = np.hstack((np.full(self.sitesL,-mu),Ed-mu,np.full(self.sitesR,-mu)))
        
        h = np.diag(muArr) \
            - np.diag( self.tunneling_array, k=1) \
            - np.diag( self.tunneling_array, k=-1)
        [self.spectrum_h0 ,self.U_dag ] = eigh(h)
        return h
    
    # finally the correlator
    def correlator(self,h_1,time):
        C = expm(1j*h_1*time) @ self.U_dag  @ self.projector() @ np.conj(self.U_dag.T) @ expm(-1j*h_1*time)
        return C
    
    # evaluating the current from the corralator
    def current(self,C,tunArr = None): # add option for diffrent tunneling values on the values 
        return np.real(1j*np.diag(C,1)- 1j*np.diag(C,-1))*self.tunneling_array  
    
    # evaluating the local density from the corralator
    def density(self,C): # add option for diffrent tunneling values on the values 
        return np.real( np.diag(C))    
    
    
    # evaluating the projector on the unoccupied states from the spectrum of h_0
    def projector(self):
      
        # Create a diagonal matrix with the eigenvalues
        P = np.diag(self.spectrum_h0) #mat will be the etas matrix (0 for negative energies and 1 for posative

        # Create a boolean mask based on the sign of the elements
        P = P > 0

        # Replace negative values with 0 and positive values with 1
        P[P] = 1
        P[~P] = 0
        return np.array(P, dtype='complex')
    
    

if __name__ == "__main__":
    
    # static parameters 
    spar = parameters()
    spar.add('sites',100)
    spar.add('mu',0)
    spar.add('tunneling',1)
    spar.add('dtunneling',0.5)
    spar.add('Ed',2)

    # dynamic parameters     
    dpar = parameters()
    dpar.add('dt',0.2)
    dpar.add('v',0.0001)
    dpar.add('timesteps',200)
    
    # construct the non-interacting class
    a = non_interacting(spar.get('sites')) 
    
    # construct the hamiltonian for time greater than zeros
    
    h_1 = a.h0(spar.get('mu'),spar.get('tunneling'),spar.get('dtunneling'),spar.get('Ed')) + a.V(dpar.get('v'))
  
    
    # initialize the data arrays 
    Current = np.empty((0,spar.get('sites')-1))
    Density = np.empty((0,spar.get('sites')))

    # run sequence for all times in steps of 0,dt,2dt ... dt*(timesteps-1) 
    for q in range(dpar.get('timesteps')):
       
        time = q * dpar.get('dt')
     
        # create the correlator at time 
        C = a.correlator(h_1, time)
       
        # add data to arrays
        Current = np.vstack((Current,a.current(C)))
        Density = np.vstack((Density,a.density(C)))
    
    
    # plot current as function of position and time
    plt.imshow(Current, extent=[-1, 1, -1, 1])
    plt.show()
    
    # plot density as function of position and time
    plt.imshow(Density, extent=[-1, 1, -1, 1])
    plt.show()
    
    # plot current from the dot to the left lead
    plt.plot(2*np.pi*Current[:,int(spar.get('sites')/2)-2]/dpar.get('v'))
    plt.show()
    
        

#%%

#%%

#%%

#%%

#%%
