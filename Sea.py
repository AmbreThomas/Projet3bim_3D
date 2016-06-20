import random
import math
from copy import *
from Shark import Shark
from Predator import Predator

class Sea :
    """attributes
    - D depth
    - zones with sharks
    - some predators
    - nb of shark in the Sea
    """
    def __init__(self,D,nb_sharks_,ori_shark,nb_pred_) : #zone_ c'est les limites de chaque zones, ori_shark c est notre requin modele de base
        self.D=D #profondeur du milieu
        self.nb_sharks=nb_sharks_
        self.population = []
        #self
        ori_shark.z = ori_shark.position_ideale
        for i in xrange(self.nb_sharks):
          self.population.append(copy(ori_shark))
          self.population[i].x = random.randint(0,500)
          self.population[i].y = random.randint(0,500)
          if (random.random() < 0.5) :
            self.population[i].sex = 1 #femelles
          else:
            self.population[i].sex = 0 #males
        self.nb_pred = nb_pred_
        self.predateurs = []
        for i in xrange (nb_pred_) :
          self.predateurs.append(Predator())

    def champsDeVision (self,individu) :
        vu=[]
        for i in xrange (len(self.population)) :
          if ((self.population[i].z >= individu.z) and (self.population[i].z <= (individu.z + 50)) and (self.population[i].x >= (individu.x - 50))and (self.population[i].x <= (individu.x + 50))and (self.population[i].y >= (individu.y - 50))and (self.population[i].y <= (individu.y + 50)) and individu != self.population[i]) :
            vu.append(self.population[i])
        return vu

    def move(self):
        for i in xrange(len(self.population)):
            pas = random.randint(-10,10)
            r = random.random()
            if r < 1/3.0:
                self.population[i].x += pas
            elif r < 2/3.0:
                self.population[i].y += pas
            else:
                self.population[i].z += pas
        for i in xrange(len(self.predateurs)) :
            pas = random.randint(-10,10)
            r = random.random()
            if r < 1/3.0:
                self.predateurs[i].x += pas
            elif r < 2/3.0:
                self.predateurs[i].y += pas
            else:
                self.predateurs[i].z += pas            

    def vieillir(self):
        for i in xrange(len(self.population)):
            self.population[i].age += 1
        for i in xrange(len(self.predateurs)) :
            self.predateurs[i].age += 1

    def mort(self):
        pop = copy(self.population)
        for i in xrange(len(self.population)):
            if (self.population[i].sex) :
                if self.population[i].age >= 22:
                    if (random.random() < 0.5):
                        pop.append(self.population[i])
            else :
                if self.population[i].age >= 18:
                    if (random.random() < 0.5):
                        pop.append(self.population[i])
                        
    def mortPredateurs (self) : 
        pop = copy(self.predateurs)
        for i in xrange(len(self.predateurs)):
              if self.predateurs[i].age >= 22:
                  if (random.random() < 0.5):
                    pop.append(self.predateurs[i])        
    
    def predation(self) :
        for i in xrange(len(self.predateurs)) :
          proies = self.champsDeVision(self.predateurs[i])
          if (len(proies) > 0) :
            random.shuffle(proies)
            self.population.pop(self.population.index(proies[0]))
          
                  

    def reproduction(self) : 
        for i in xrange(len(self.population)) :
          if (self.population[i].sex == 1) :
            entourage = self.champsDeVision(self.population[i])
            if (len(entourage) >0) :
              cop = []
              for j in xrange(len(entourage)) :
                if (entourage[j].sex == 0) :
                  cop.append(entourage[j])
              random.shuffle(cop)
              self.population.append(self.moyenneDeuxRequins(self.population[i],entourage[0]))
              
            
    def moyenneDeuxRequins (self, r1, r2) :
        requinou = copy(r1)
        requinou.lateral_bio=(r1.lateral_bio + r2.lateral_bio)/2
        requinou.ventral_bio=(r1.ventral_bio + r2.ventral_bio)/2
        i=0
        while i < len(requinou.tab_ventral) :
          requinou.tab_ventral[i] = (r1.tab_ventral[i] + r2.tab_ventral[i] )/2.0
          i += 1
        i=0
        while i < len(requinou.tab_lateral) :
          requinou.tab_lateral[i] = (r1.tab_lateral[i] + r2.tab_lateral[i] )/2.0
          i += 1
        requinou.coef_biolum_ventral = int((r1.coef_biolum_ventral + r2.coef_biolum_ventral)/2)
        requinou.coef_biolum_lateral = int((r1.coef_biolum_lateral + r2.coef_biolum_lateral)/2)
        requinou.cases_biolum_ventral = int((r1.cases_biolum_ventral + r2.cases_biolum_ventral)/2)
        requinou.cases_biolum_lateral = int((r1.cases_biolum_lateral + r2.cases_biolum_lateral)/2)
        requinou.calculProfondeur() #p ideale
        requinou.mise_jour_attributs()
        requinou.age = 0
        if (random.random() < 0.5) :
          self.population[i].sex = 1 #femelles
        else:
          self.population[i].sex = 0 #males
        return requinou
