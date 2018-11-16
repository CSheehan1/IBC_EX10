#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 15:11:51 2018

@author: ColinSheehan
"""

import numpy
import pandas
from scipy.optimize import minimize
from scipy.stats import norm
from plotnine import *
import scipy
import scipy.integrate as spint
ls
datafile=pandas.read_csv("data.txt")
datafile
y=datafile.iloc[:,1]
x=datafile.iloc[:,0]
y
x
lindata=pandas.DataFrame({'x':x,'y':y})
ggplot(datafile,aes(x='x',y='y'))+geom_point()+theme_classic()
def linmod(p,obs):
    B0=p[0]
    B1=p[1]
    sigma=p[2]
    expected=B0+B1*obs.x
    lin=-1*norm(expected,sigma).logpdf(obs.y).sum()
    return lin
initialGuess=numpy.array([1,1,1])
linfit=minimize(linmod,initialGuess,method="Nelder-Mead",options={'disp': True},args=lindata)
print(linfit)
def nonlinmod(p,obs):
    L0=p[0]
    L1=p[1]
    L2=p[2]
    sigma=p[3]
    expected2=L0+L1*obs.x+L2*obs.x*obs.x
    quad=-1*norm(expected2,sigma).logpdf(obs.y).sum()
    return quad
initialGuess2=numpy.array([1,1,1,1])
quadfit=minimize(nonlinmod,initialGuess2,method="Nelder-Mead",options={'disp': True},args=lindata)
print(quadfit)


    