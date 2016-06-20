import random
import math
from copy import *
from Shark import Shark
from Zone import Zone

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
          self.population.append(ori_shark)
          self.population[i].x = random.randint(0,500)
          self.population[i].y = random.randint(0,500)
        












