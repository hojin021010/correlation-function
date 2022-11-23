
import math
class baseratecor:
    
    def __init__():
        
        
        
    def mean(data):
        result = 0
        len_data = len(data)
        for i in data:
          result += i
        return result / len(data)  

    def correlation(data1,data2):
        meanData1 = mean(data1)
        meanData2 = mean(data2)
        up = 0
        for i in range(len(data1)):
            up += (data1[i]-meanData1) * (data2[i]-meanData2)
        bottom = 0
        data1Bottom = 0
        data2Bottom = 0
        for i in data1:
            data1Bottom += (i - meanData1)**2
        for i in data2:
            data2Bottom += (i - meanData2)**2
        bottom = math.sqrt(data1Bottom) * math.sqrt(data2Bottom)
        return up/bottom

 
 