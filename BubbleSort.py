def myBubbleSort(someList):

    while True:
        
        for each in range(1, len(someList)):
        
            if someList[each] < someList[each - 1]:
            
                someList[each], someList[each - 1] = someList[each - 1], someList[each]
            
                break
        else:
        
            break

    
    print "New list", someList
        

myList = [1,4,8,3,2,9,5,0,6,7] 

myBubbleSort(myList)