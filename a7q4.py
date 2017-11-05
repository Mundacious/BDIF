# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:19:10 2017

@author: Anujay Shah
"""

import numpy as np

Q = np.zeros((6,6))
Q[0,]=[0.0,0.5,0.5,0.0,0.0,0.0]
Q[1,]=[0.0,0.0,1.0,0.0,0.0,0.0]
Q[2,]=[1.0,0.0,0.0,0.0,0.0,0.0]
Q[3,]=[0.5,0.0,0.5,0.0,0.0,0.0]
Q[4,]=[0.0,0.0,1.0,0.0,0.0,0.0]
Q[5,]=[0.0,0.5,0.0,0.0,0.5,0.0]

e = .01
d = 6.0
qb = (1-e)*Q+(e/d)

mo = (1/d)*np.ones(6)
T = 1000

for t in range(T):
    mn = mo.dot(qb)
    mo = mn
    
print(mn)

for j in range(21):
    e = j/(20*1.0)
    qb = (1-e)*Q+(e/d)
    mo = (1/d)*np.ones(6)
    T = 1000
    for t in range(T):
        mn = mo.dot(qb)
        mo = mn
    print(mn)