
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


S = Sea(1200, 400, req1,150)

i=0 
print
while i < 1000 :
  print i
  S.move()
  S.mort()
  S.mortPredateurs()
  S.predation()
  S.reproduction()
  S.vieillir()
  i+=1

#S.moyenneDeuxRequins(S.population[10],S.population[11])
#print len(S.champsDeVision(S.population[10]))


