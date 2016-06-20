import random
import math
from copy import *
from Shark import Shark

class Sea :
    """attributes
    - D depth
    - zones with sharks
    - some predators
    - nb of shark in the Sea
    """
    def __init__(self,D,nb_sharks_,ori_shark) : #zone_ c'est les limites de chaque zones, ori_shark c est notre requin modele de base
        self.D=D #profondeur du milieu
        self.nb_sharks=nb_sharks_
        self.population = []
        ori_shark.z = ori_shark.position_ideale
        for i in xrange(self.nb_sharks):
          self.population.append(copy(ori_shark))
          self.population[i].x = random.randint(0,500)
          self.population[i].y = random.randint(0,500)
          if (random.random() < 0.5) :
            self.population[i].sex = 1 #femelles
          else:
            self.population[i].sex = 0 #males

    def champsDeVision (self,individu) :
        vu=[]
        for i in xrange (len(self.population)) :
          if ((self.population[i].z >= individu.z) and (self.population[i].z <= (individu.z + 50)) and (self.population[i].x >= (individu.x - 50))and (self.population[i].x <= (individu.x + 50))and (self.population[i].y >= (individu.y - 50))and (self.population[i].y <= (individu.y + 50))) :
            vu.append(self.population[i])
        return vu

    def move(self):
        for i in xrange(len(self.population)):
            pas = random.randint(-5,5)
            r = random.random()
            if r < 1/3.0:
                self.population.x += pas
            elif r < 2/3.0:
                self.population.y += pas
            else:
                self.population.z += pas
            

    def vieillir(self):
        for i in xrange(len(self.population)):
            self.population[i].age += 1

    def mort(self):
        pop = copy(self.population)
        for i in xrange(len(self.population)):
            if self.population[i].sex == 1:
                if self.population[i].age >= 22:
                    if (random.random() < 0.5):
                        pop.append(self.population[i])
            if self.population[i].sex == 0 :
                if self.population[i].age >= 18:
                    if (random.random() < 0.5):
                        pop.append(self.population[i])






