#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 17:23:31 2020

@author: tianyi sun
"""



        
def AI_analysis(dataArr, datatype = "nomal"):
    try:
        res = []
        if datatype ==  "bp":
            avg = []
            sum1 = 0
            sum2 = 0
            for val in dataArr:
                sum1 = sum1 + int(val[0])
                sum2 = sum2 + int(val[1])
            avg.append(sum1 // len(dataArr))
            avg.append(sum2 // len(dataArr))

        else:
            avg = 0
            sum = 0
            for val in dataArr:
                sum = sum + int(val)
            avg = sum // len(dataArr)
        res.append(avg)    
        return res           
    except:
        return "AI predicted fail!!!"
  
    

    
        