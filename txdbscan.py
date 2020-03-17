#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:06:00 2020

@author: TX
"""

import numpy as np
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=200, noise=0.05, random_state=0)
from sklearn.metrics import accuracy_score

def NB_get(DB,q,eps):
    NB=set()
    Q=DB[q]
    for p,P in enumerate(DB):
        if np.linalg.norm(Q-P)<eps and p!=q:
            NB.add(p)
    return NB
def TXDBSCAN(DB,eps,minPts):
    V=set() # Visited
    C=0
    L=[0]*len(DB)
    for p,P in enumerate(DB):
        if L[p]!=0:
            continue
        NB=NB_get(DB,p,eps)
        if len(NB)<minPts:
            L[p]=-1
            V.add(p)
            continue
        C=C+1
        L[p]=C
        V.add(p)
        while NB:
            pn=NB.pop()
            if L[pn]==-1 or L[pn]==0:
                L[pn]=C
                V.add(pn)
            NB_pn=NB_get(DB,pn,eps)
            if len(NB_pn)>=minPts:
                NB=NB.union(NB_pn-V)
    return L

dbscan_pred=TXDBSCAN(X,0.2,4)
dbscan_score=accuracy_score(y, [x-1 for x in dbscan_pred])

import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,4))
plt.text(0.5,0.5,'BDSCAN',ha='center',va='center',size=20,alpha=0.5)
plt.scatter(X[:,0],X[:,1],c=dbscan_pred,cmap='bwr')
plt.show()
