import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plotrate(rate,price):
     plt.plot(rate,price,marker='o')
     plt.grid()
     plt.xticks(rate)
     plt.yticks(price)

def myplotshow(rate,price):
     result_price= price * rate
     plotrate(rate,result_price)

def bsp(price=0):
     rate = np.arange(0.9,1.1,0.02)
     myplotshow(rate,price)

def withdraw(price=0):
     rate =1- np.array([0.33,0.38,0.50,0.62,0.68])
     myplotshow(rate,price)

def invest(interest):
     rate = np.arange(0.01,0.1,0.01)
     total = interest/rate
     plotrate(rate,total)


def future_value(init=0,rate=1,period=1):
    time_range = np.arange(period)
    future = init *rate**time_range
    plotrate(time_range,future)

def plan_30_30():
    """
     init 30
     rate 1.05-1.20
     rate 36month
    """
    for x in np.arange(1.05,1.20,0.01):
	future_value(30,x,36)

def UpDownRate():
    up = np.arange(1.02,1.60,0.02)
    down = 1.0/up
    plotrate(up,down)
    

