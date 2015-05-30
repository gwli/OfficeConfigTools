import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def bsp(price=0):
     rate = np.arange(0.9,1.1,0.02)
     plt.plot(rate,price*rate,marker='o')
     plt.grid()
     plt.xticks(rate)
     plt.yticks(price*rate)
