import numpy as np 

def medianOfArray(list1, list2):
    list1 += list2 
    print(np.median(list1))

medianOfArray([1,3], [2])

def mergeLists(*arg):
    finalList = []
    for i in arg:
        finalList += i 
    finalList = sorted(finalList)
    print(finalList)

mergeLists([1,2,3,5], [0, 4])