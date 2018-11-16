#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 00:16:57 2018

@author: ColinSheehan
"""
def competitionsim(y,t0,Ra,Rb,Caa,Cab,Cba,Cbb,):
    A=y[0]
    B=y[1]
    dAdt=Ra*(1-A*Caa-B*Cab)*A
    dBdt=Rb*(1-B*Cbb-A*Cba)*B
    return (dAdt,dBdt)
#case1: a12<a11 and a21<a22, should produce coexistence
times=range(1,100)
y0=[0.1,0.1]
params=(0.5,0.5,1,0.5,0.5,0.7)
sim1=spint.odeint(func=competitionsim,y0=y0,t=times,args=params)
sim1DF=pandas.DataFrame({"t":times,"A":sim1[:,0],"B":sim1[:,1]})
ggplot(sim1DF,aes(x="t",y="A"))+geom_line()+geom_line(sim1DF,aes(x="t",y="B"),color='red')+theme_classic()
#case2:a12>a11 and a21<a22 should disrupt coexistence
params=(0.5,0.5,0.5,1,0.5,0.7)
sim1=spint.odeint(func=competitionsim,y0=y0,t=times,args=params)
sim1DF=pandas.DataFrame({"t":times,"A":sim1[:,0],"B":sim1[:,1]})
ggplot(sim1DF,aes(x="t",y="A"))+geom_line()+geom_line(sim1DF,aes(x="t",y="B"),color='red')+theme_classic()
#case3:a12<a11 and a21>a22 should also disrupt coexistence
params=(0.5,0.5,1,0.5,0.7,0.5)
sim1=spint.odeint(func=competitionsim,y0=y0,t=times,args=params)
sim1DF=pandas.DataFrame({"t":times,"A":sim1[:,0],"B":sim1[:,1]})
ggplot(sim1DF,aes(x="t",y="A"))+geom_line()+geom_line(sim1DF,aes(x="t",y="B"),color='red')+theme_classic()
#case4:a12<a11 and a21<a22 should also disrupt coexistence
params=(0.5,0.5,0.5,1,0.7,0.5)
sim1=spint.odeint(func=competitionsim,y0=y0,t=times,args=params)
sim1DF=pandas.DataFrame({"t":times,"A":sim1[:,0],"B":sim1[:,1]})
ggplot(sim1DF,aes(x="t",y="A"))+geom_line()+geom_line(sim1DF,aes(x="t",y="B"),color='red')+theme_classic()