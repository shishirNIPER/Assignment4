# -*- coding: utf-8 -*-
"""Untitled29.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RtBO-mpBT1Q53uYMZRZxL66ZAn1aFeRj
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

plt.axis([-3,3,-3,3])

plt.xticks(np.arange(-3, 3, 1))
plt.yticks(np.arange(-3, 3, 1))

plt.axis('on')
plt.grid(True)

P = np.array([2,0])
Q = np.array([0,-2])
A = np.array([0,0])
B = np.array([1,1])


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

  #Generating all lines
x_PQ = line_gen(P,Q) 
x_AB = line_gen(A,B) 

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
#plt.axis('equal')
plt.legend(loc='upper right')


plt.text(2,0,'P(2,0)')
plt.text(0,-2,'Q(0,-2)')
plt.text(0,0,'A(0,0)')
plt.text(1,1,'B(1,1)')