#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:52:05 2020

@author: TX
"""

import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot([0,0.5,1],[1,0,1],linestyle='-',label='line#1')
plt.legend(loc='upper center',frameon=True)
plt.subplot(1,2,2)
plt.plot([0,0.5,1],[0.0,0.8,1],linewidth=4,label='line#2')
plt.legend(loc='upper center',frameon=True)
plt.show()

import matplotlib.pyplot as plt
fig,axes=plt.subplots(2,1)
for i,ax in enumerate(axes.flat):
    ax.set(xticks=[0,i+1],yticks=[0,i+1])
    s='subplot({})'.format(i)
    ax.text(1,1,s,ha='right',va='top',size=20,alpha=0.5)
plt.show()
