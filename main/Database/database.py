import json


def createO2table():
    fp = open("./Database/oxygen",'a')  
    fp.close( )

def createBPtable():
    fp = open("./Database/bp",'a')  
    fp.close( )

def createPulsetable():
    fp = open("./Database/pulse",'a')  
    fp.close( )

def parseJsonfile():#(jsonfile):
    with open('data') as json_file:
        data = json.load(json_file)
    
    for jsonfile in data['data']:    
        if jsonfile['name'] == "pulse":
            storePulsedata(jsonfile['values'])
        elif jsonfile['name'] == "bp":
            storeBPdata(jsonfile['values'])
        elif jsonfile['name'] == "oxygen":
            storeO2data(jsonfile['values'])
    
def storeO2data(O2_data):
    try:
        file_object = open('./Database/oxygen', 'a')
        file_object.write(str(O2_data)+'\n')
        file_object.close()
        return "store O2 data success"
    except Exception as e:
        # return "store O2 data failed: "+ e
        return "stored failed"

def storeBPdata(BP_data):
    try:
        file_object = open('./Database/bp', 'a')
        file_object.write(str(BP_data[0])+' '+str(BP_data[1])+'\n')
        file_object.close()
        return "store BP data success"
    except Exception as e:
        return "store BP data failed"
        
def storePulsedata(Pulse_data):
    try:
        file_object = open('./Database/pulse', 'a')
        file_object.write(str(Pulse_data)+'\n')
        file_object.close()
        return "store Pulse data success"
    except Exception as e:
        return "store Pulse data failed"
        
def getO2data():
    try:
        with open('./Database/oxygen', 'r') as fp:
            lines = fp.readlines()
        return lines
        print("get O2 data success")
    except Exception as e:
        print("get O2 data failed: "+e)
        
def getBPdata():
    try:
        with open('./Database/bp', 'r') as fp:
            lines = fp.readlines()
        return lines
        print("get BP data success")
    except Exception as e:
        print("get BP data failed: " + e)
    
def getPulsedata():
    try:
        with open('./Database/pulse', 'r') as fp:
            lines = fp.readlines()
        return lines
        print("get Pulse data success")
    except Exception as e:
        print("get Pulse data failed: "+e)
        
def get_whole_data(filename):
    try:
         with open(os.path.join('', filename)) as f:
             s=f.read()
             f.close()
         return str(s)

    except Exception as e:
        print('----------------')
        return e

if __name__ == '__main__':
    createO2table()
    createBPtable()  
    createPulsetable()
    
    #parseJsonfile()
    print(getO2data())
