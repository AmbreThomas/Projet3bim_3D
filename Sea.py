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
        self.cap_limite = 600.0

    def champsDeVision (self,individu) :
        vu=[]
        for i in xrange (len(self.population)) :
          if ((self.population[i].z >= individu.z) and (self.population[i].z <= (individu.z + 50)) and (self.population[i].x >= (individu.x - 50))and (self.population[i].x <= (individu.x + 50))and (self.population[i].y >= (individu.y - 50))and (self.population[i].y <= (individu.y + 50)) and individu != self.population[i]) :
            vu.append(self.population[i])
        return vu

    def move(self):
        for i in xrange(len(self.population)):
            self.population[i].mise_jour_attributs()
            pas = random.randint(-10,10)
            m = random.random()
            if self.population[i].fit_position > 60 : 
              p_move=0.8
            else :
              p_move =0.1
            r = random.random()
            if r<p_move : 
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
        pop = []
        for i in xrange(len(self.population)):
            if (self.population[i].sex) :
                if self.population[i].age >= 22:
                    if (random.random() < 0.5):
                        pop.append(self.population[i])
                else :
                  pop.append(self.population[i])
            else :
                if self.population[i].age >= 18:
                    if (random.random() < 0.5):
                        pop.append(self.population[i])
                else :
                  pop.append(self.population[i])
        self.population = pop
                        
    """def mortPredateurs (self) : 
        pop = []
        for i in xrange(len(self.predateurs)):
              if self.predateurs[i].age >= 22:
                  if (random.random() < 0.5):
                    pop.append(self.predateurs[i])   
              else :
                pop.append(self.population[i])
        self.predateurs = pop"""
    
    def capaciteLimite(self) :
        pop=[]
        for i in xrange(len(self.population)):
          if ((random.random() + 1) > len(self.population)/self.cap_limite) :
            pop.append(self.population[i])
        self.population = pop
          
    
    def predation(self) :
        for i in xrange(len(self.predateurs)) :
          proies = self.champsDeVision(self.predateurs[i])
          if (len(proies) > 0) :
            fitness=[] #pour pouvoir comparer les fitness des requins
            for i,a in enumerate (proies) :
              fitness.append(a.fit_position * a.lateral_bio) 
            
            fmax=max(fitness)
            death_candidates=[] #leur indice
            for j,a in enumerate (proies) :
              if (a.fit_position * a.lateral_bio == fmax) : 
                death_candidates.append(j)
                random.shuffle(death_candidates) # on tue aleatoirement un des requins qui a la fitness position max
            self.population.pop(self.population.index(proies[death_candidates[0]]))
            #print "a tue", fmax    
                  

    def reproduction(self) : 
        #print len(self.population)
        for i in xrange(len(self.population)) :
          if (self.population[i].sex == 1 and self.population[i].age > 5 ) :
            entourage = self.champsDeVision(self.population[i])
            if (len(entourage) >0) :
              cop = []
              lat =[] #pour pouvoir comparer les lat des requins
              for j,a in enumerate (entourage) :
                if (a.sex == 0 and a.age > 4) :
                  d=abs(self.population[i].lateral_bio-a.lateral_bio)
                  lat.append(d)
              if (len(lat) >0 ) :    
                latmin=min(lat)
                for j,a in enumerate (entourage):
                  if (latmin == abs(self.population[i].lateral_bio-a.lateral_bio)) :
                    cop.append(a)
                random.shuffle(cop)
                self.population.append(self.moyenneDeuxRequins(self.population[i],cop[0]))
                self.population[-1].toMute()
              
        #print len(self.population)
              
            
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
          requinou.sex = 1 #femelles
        else:
          requinou.sex = 0 #males
        return requinou
