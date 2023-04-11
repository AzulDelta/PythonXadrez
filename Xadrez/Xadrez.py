from ctypes.wintypes import INT
from pickle import STRING
from tokenize import String
import numpy as np
import random as random

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from XadrezFuncoes import *
from XadrezClasses import *

colorama_init()

lista = []

try


#tabuleiro = np.empty([8, 8],dtype=str)
tabuleiro = np.full([2,8],'  ',dtype=str)
#tabuleiro.fill("AA");

#tabuleiro.T[..., 1] = ["BP"]

#tabuleiro.T[..., 6] = ["WP"]

#array = np.zeros((8,8),dtype=STR)
#array.fill("AA")
#print(array)

RenderizarTabuleiro(tabuleiro,"")
