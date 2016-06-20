
import random
from Sea import Sea
from Shark import Shark
from Tkinter import *
import matplotlib.pyplot as plt
import copy


#CREER ICI LE REQUIN MODELE
req1 = Shark([800, 999])
req1.ventral_lateralBio("requin_lateral.jpg", "requin_ventral.jpg")

S = Sea(1200, 400, req1)


