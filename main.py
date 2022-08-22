import numpy as np 

def medianOfArray(*args):
    finalList = []
    for i in args:
        finalList += i
    print(np.median(finalList))

medianOfArray([1,3], [2], [4], [9])

def mergeLists(*arg):
    finalList = []
    for i in arg:
        finalList += i 
    finalList = sorted(finalList)
    print(finalList)

mergeLists([1,2,3,5], [0, 4])