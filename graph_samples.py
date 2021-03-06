                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ww# -*- coding: utf-8 -*-
"""
Graph samples

Created on Thu Aug 15 17:26:20 2019

@author: Victoria Cook

To use, repoint the filename variable to a 2019 matchScoutData excel file.
"""

filename = r'C:\Users\stat\Documents\FRC\2019\matchScoutData-CMO.xlsx'

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(filename)

print(df.columns)

print('Maximum scored objects in a match', df.totalscored.max())


def basicHist(df):
    '''
    This function will plot a basic histogram using default settings of the
    total game objects scored.
    
    Each bar will show the count of the number of data values in the bin.
    
    Since the values are all integers, the lower bound of the bin is the value
    counted for that bar.
    '''
    plt.hist(df.totalscored)
    
    plt.show()

def cleanBasicHist(df):
    '''
    This is the same data as basicHist, but the color is explicitly specified.
    The bins are explicitly specified (note that if the bins don't cover 
    the max value, you will miss information).  I've centered the bars on the
    lower bound, which is the value since the first bin is [0-1) 
    (i.e. 0 is in, 1 is not).  I've made the bins half as wide, and I set the 
    vertical axis to show the density, which is the number of measurements in 
    the bin divided by the number of measurements in the data.
    '''
    plt.hist(df.totalscored,color="teal",bins = [0,1,2,3,4,5,6,7,8,9,10], 
             align = 'left',rwidth=0.5, density = True)
    
    plt.show()
    
def complexSubplots(df):    
    '''
    For this, I took the same graph settings and made subplots showing total
    objects scored, teleop cargo scored, and teleop hatch panels scored in a 
    three row, one column display, and put some y-axis labels on.
    '''
    plt.figure()
    plt.subplots(sharey = 'col')
    plt.subplot(311)
    plt.hist(df.totalscored,color="blue",bins = [0,1,2,3,4,5,6,7,8,9,10],
             align = 'left',rwidth=0.5, density = True)
    plt.ylabel('Total Objects')
    plt.subplot(312)
    plt.hist(df.telecargo, color="green",bins = [0,1,2,3,4,5,6,7,8,9,10],
             align = 'left',rwidth=0.5, density = True)
    plt.ylabel('Cargo')
    plt.subplot(313)
    plt.hist(df.telehatch, color="red",bins = [0,1,2,3,4,5,6,7,8,9,10],
             align = 'left',rwidth=0.5, density = True)
    plt.ylabel('HP')
    
    plt.show()

def basicScatter(df):
    '''
    For this, we're going to look at hatches vs. cargo in each team/match
    '''
    
    plt.scatter(df.telecargo, df.telehatch)
    
    plt.show()
    
def moredefScatter(df):
    '''
    Let's see if we can make it more obvious when we're overplotting the same point
    '''
    plt.scatter(df.telecargo, df.telehatch, alpha=.05, s=80)
    plt.axis([-1,10,-1,10])
    
    plt.show()
    
def betterScatter(df):
    
    pointcountdf = pd.pivot_table(df, index=df.telecargo, columns=df.telehatch, aggfunc=np.count_nonzero)
    print(pointcountdf)
    
    
    plt.scatter(pointcountdf.index(), pointcountdf.columns(), s=pointcountdf.values())
    plt.show()