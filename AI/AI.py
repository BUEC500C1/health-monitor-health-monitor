#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 17:23:31 2020

@author: tianyi sun
"""
# need to connect to db part
import database as db

def AI_compute(data, type):
    if type == "O2":
        try:
            num = sum(data) / len(data)
            print("AI Module predicting O2 data....")
            return num
        except:
            print("Call AI module fail!!!!!")
    elif type == "pulse":
        try:
            #call AI module 
            num = sum(data) / len(data)
            print("AI Module predicting Pulse data....")
            return num
        except:
            print("Call AI module fail!!!!!")   
    elif type ==  "bloodPressure":
        try:
            #call AI module 
            num = sum(data) / len(data)
            print("AI Module predicting blood pressure data....")
            return num
        except:
            print("Call AI module fail!!!!!")   
    else:
         print("No data to AI module!!!")
 
def preprocess(data):
    #change string inside file to int list
    #'[20,30,40]' to [20,30,40] 
    dataList = list(data.split("\n"))
    numList = []
    for s in dataList:
        lineList = s.split(" ")
        for item in lineList:
            numList.append(int(item))
    return numList    
 
def predictO2(O2data):
    try:
        data = preprocess(O2data)
        result = AI_analysis(data, "O2")
        return result
    except:
        print("O2 predict fail!!!!")
    

def predictPulse(pulseData):
    try:
        data = preprocess(pulseData)
        result = AI_analysis(data, "pulse")
        return result
    except:
        print("Pulse predict fail!!!!")
    
        
def predictBloodPressure(bloodPressureData):
    try:
        data= preprocess(bloodPressureData)
        result = AI_analysis(data, "bloodPressure")
        return result
    except:
        print("Blood pressure predict fail!!!!")

        
def connectDb(Type):
    #call database function
    #O2 data
    if Type == "O2": 
        try:
            O2data = db.getO2data()
            return O2data
        except:
            print("Fetch O2 data fail!!!!")
    #BP data 
    if Type == "BP": 
        try:
            BPdata = db.getBPdata()
            return BPdata  
        except:
            print("Fetch BP data fail!!!!")
            
    #pulse data 
    if Type == "pulse":
        try:
            Pulsedata = db.getPulsedat()
            return Pulsedata
        except:
            print("Fetch Pulse fail!!!!")
        
def AI_analysis():
    o2 = connectDb("O2")
    bp = connectDb("BP")
    pulse = connectDb("pulse")
    nextO2 = predictO2(o2)
    nextbp = predictBloodPressure(bp)
    nextpulse = predictPulse(pulse)
    #to json format
    list = []
    tmp = {}
    tmp['name'] = 'pulse'
    tmp['value'] = list(nextpulse)
    list.append(tmp)
    
    tmp = {}
    tmp['name'] = 'oxygen'
    tmp['value'] = list(nextO2)
    list.append(tmp)   
    
    tmp = {}
    tmp['name'] = 'bp'
    tmp['value'] = list(nextbp)
    list.append(tmp) 
    res = {}
    res['data'] = list
    try:
        file_object = open('data', 'a')
        file_object.write(str(res)+'\n')
        file_object.close()
        return str(res)
    except:
        return "Store to File fail!!!"
  
    
if __name__ == '__main__':
    AI_analysis()
    
        