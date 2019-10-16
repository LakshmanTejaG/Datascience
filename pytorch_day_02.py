# -*- coding: utf-8 -*-
"""PyTorch_Day_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FrWSeNrnu0h2kefVJSzywImNudptKCBn
"""

import torch

# 3D matrix vectors creation
Teja = torch.arange(27).view(3,3,3)
print(Teja)

Sirisha = torch.arange(27).view(3,3,3)
print(Sirisha)

# Slicing the 3D vectors
print(Teja[0,0,1])
print(Teja[1,2,2])

# Vector multiplication
Diff = torch.matmul(Teja,Sirisha)
print(Diff)

Teja @ Sirisha

x = torch.tensor(2.0, requires_grad=True)
z = torch.tensor(1.0, requires_grad=True)
y = 9*x**4 + 2*x**3 + 3*x**2 + 6*x+1
a = x**3 + z**2
y.backward()
a.backward()
x.grad
z.grad

import torch

m = torch.tensor(3.0, requires_grad=True)
c = torch.tensor(2.0, requires_grad=True)

y = m*x + c 

def forward(x):
  y = m*x + c
  return y

x = torch.tensor(([2],[4]))
forward(x)