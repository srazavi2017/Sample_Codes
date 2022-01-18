import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv, math, ast, copy, os, pickle, subprocess
from IPython.display import display, HTML
from timeit import default_timer as timer
import time
import warnings, json
import subprocess, os
import seaborn as sns
from scipy.io import wavfile
import wave, struct
import logging
from itertools import combinations, permutations

VL = []
for i in permutations([3,3,4,1]):
    Li = list(i)
    Li.insert(0, 0)
    print(Li)
    c = 0
    for j in range(len(Li)-1):
        for k in range(len(Li)-1-j):
#             print(j,k)
            if Li[-1-j] > Li[-1-j-k-1]:
                c += 1
            else:
                c += 1
                break
    VL.append(c)
VL
