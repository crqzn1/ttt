#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:05:47 2020

@author: TX
"""

from sklearn.cluster import KMeans
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=200, noise=0.05, random_state=0)
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
y_pred = kmeans.predict(X)

import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,4))
plt.text(0.5,0.5,'kmeans',ha='center',va='center',size=20,alpha=0.5)
plt.scatter(X[:,0],X[:,1],c=y_pred,cmap='bwr')
plt.show()
