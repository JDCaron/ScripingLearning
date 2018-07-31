def quickSort(someList):
    
    if len(someList) < 2:
        return someList
    else:
        
        pivot = someList[0]
        rest = someList[1:]
                
        smalls = [i for i in rest if i <= pivot]
        bigs = [i for i in rest if i > pivot]

        return quickSort(smalls) + [pivot] + quickSort(bigs)
            
myList = [5,3,9,7,10,4,1,6,2,8,0]
print(myList)
myList = quickSort(myList)
print(myList)