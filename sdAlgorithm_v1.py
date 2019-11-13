#! /usr/bin/env python
# Senior Design Algorithm #1
# Author: Casey Bruno, Rutwika Anumula, Thao Vo

import numpy as np
import sys


def algorithmAS(argv):
    
    RRintervals = list(argv[0])
    gender = str(argv[1])
    age = int(25)
    
    if RRintervals[0] < 1:
        RRintervals = RRintervals*1000
    
    temp = 0
    for i in range(1,len(RRintervals)):
        diff = RRintervals[i] - RRintervals[i-1]
        diff2 = diff ** 2
        temp = temp + diff2
        
    print(temp)
    average_diff = temp/len(RRintervals)
    RMSSD = np.sqrt(average_diff)
    
    logRMSSD = np.log(RMSSD)
    score = (logRMSSD/6.5)*100
    print(score, gender, age)
    print(score, min_warn, max_warn)
    
    
    if (warn_min < score) and (warn_max > score):
        print("Pull over, you are drowsy!")
        return True
    else:
        print("Continue driving, you super star~")
        return False
    
    
def algorithmMM(argv):
    
    RRintervals = list(argv[0])
#    gender = str(argv[1])
#    age = int(25)
    warn_min = int(argv[1])
    warn_max = int(argv[2])
    
    if RRintervals[0] < 1:
        RRintervals = RRintervals*1000
    
    temp = 0
    for i in range(1,len(RRintervals)):
        diff = RRintervals[i] - RRintervals[i-1]
        diff2 = diff ** 2
        temp = temp + diff2
        
#    print(temp)
    average_diff = temp/len(RRintervals)
    RMSSD = np.sqrt(average_diff)
    
    logRMSSD = np.log(RMSSD)
    score = (logRMSSD/6.5)*100
#    print(score, warn_min, warn_max)
    
    if (warn_min < score) and (warn_max > score):
        print("Pull over, you are drowsy!")
        return True
    else:
        print("Continue driving, you super star~")
        return False
        
        
if __name__=='__main__':
    
#    main([[985, 875, 655, 792, 823], 'Male', 22])   
#    main(sys.argv[1:])
#    algorithmAS([[985, 875, 655, 792, 823], 'Male', 22])
    algorithmMM([[985, 875, 655, 792, 823], 58, 78])
    