#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:19:20 2023

@author: Daniel & Tali
"""

class parameters:
    
    # initalization of the class
    def __init__(self):
        self.params = {}
        
    # redefine the string representation of the class
    def __str__(self):
        result=""
        for key in self.params.keys():
            result += "," + key + "=" + ("%g" % self.params[key])
        return result
    
    # add a new parameter
    def add(self,name,value):
        self.params[name] = value
    
    # get value of parameter
    
    def get(self,name):
        return self.params[name]

if __name__ == "__main__":
    a = parameters()
    a.add('Sites',20)
    a.add('tunneling', 1)
    a.add('coupling', 0.1)
    a.add('Ed',-0.5)
    a.add('U',3)
    b = str(a)
    print(b)
    

#%%

#%%
