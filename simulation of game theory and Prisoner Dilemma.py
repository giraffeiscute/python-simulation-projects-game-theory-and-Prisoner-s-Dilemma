# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:46:53 2021

@author: jason
"""

import nashpy as nash
import numpy as np
import axelrod as axl

# Create the game with the payoff matrix
A = np.array([[-4,8],[0,4]]) # A is the row player
B = np.array([[-4,0],[8,4]]) # B is the column player
game1 = nash.Game(A,B)
print(game1)
# Find the Nash Equilibrium with Support Enumeration
equilibria = game1.support_enumeration()
for eq in equilibria:
    print(eq)
 
'''
# Create the payoff matrix
companyA = np.array([[4,0],[0,2]]) 
companyB = np.array([[2,0],[0,9]]) 
game2 = nash.Game(companyA,companyB)
# Find the Nash Equilibrium with Support Enumeration
equilibria = game2.support_enumeration()
for eq in equilibria:
    print(eq)
# Calculate Utilities
sigma_r = np.array([.81818182,.18181818])
sigma_c = np.array([.33333333,.66666667])
pd = nash.Game(companyA, companyB)
print(pd[sigma_r, sigma_c]) 
'''      
'''
# Case 1: Game is played for a finite number of times (say 10)
players = (axl.Defector(), axl.Defector())              
match1 =   axl.Match(players, turns =10)                          
match1.play()
'''
'''
players = (axl.TitForTat(), axl.Random())               # Player A plays of titfortat and player B Random strategy
match2 =   axl.Match(players, turns =20)                          # play for 20 turns
match2.play()
''' 
    
    
    
    