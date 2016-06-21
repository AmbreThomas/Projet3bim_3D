
import random
from Sea import Sea
from Shark import Shark
from Tkinter import *
import matplotlib.pyplot as plt
import copy
import numpy as np


#CREER ICI LE REQUIN MODELE
req1 = Shark([800, 999])
req1.ventral_lateralBio("requin_lateral.jpg", "requin_ventral.jpg")
#req2 = copy.copy(req1) 
#print len(req1.tab_ventral), len(req2.tab_ventral)


S = Sea(1200, 400, req1,400)

i=0 
#print len(S.population), len(S.predateurs)
result=[]
temps=[]
while i < 1000 :
  print i
  S.move()
  S.mort()
  #S.mortPredateurs()
  S.predation()
  if len(S.population)  == 0 :
    break
  if i%12 == 0 :
    S.reproduction()
    S.vieillir()
  if len(S.population) > S.cap_limite :
    S.capaciteLimite()
  if len(S.population)  == 0 :
    break
  i+=1
  result.append(len(S.population))
  temps.append(i)
  #print len(S.population), len(S.predateurs)
 
plt.plot(temps,result)
plt.show()

#S.moyenneDeuxRequins(S.population[10],S.population[11])
#print len(S.champsDeVision(S.population[10]))


