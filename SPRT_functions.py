#GTC ==1.2.0
from GTC import *
import numpy as np

class PRT():
    def __init__(self,model=None,numer=None):
        self.model=model
        self.numer=numer
        self.R0=None
        self.Wt=np.array([])

    def metoda1(self):
        print("model to", self.model)
        print("numer to", self.numer)