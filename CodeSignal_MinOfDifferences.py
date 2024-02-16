def solution(a):

    #Start at -1 index
    indexOfMinimum = -1
    #min-sum can be an infinite float
    minimalSum = float('inf')

    #len() returns the length of an array; counting starts at 1 not at 0
    #range() creates an array that contains a range of numbers that start at zero and 
    #ends at len(a), where a is excluded from the array; each element in the array increments by 1
    #So if a = [1, 1, 3, 4] then range(len(a)) outputs the following: [0,1,2,3]
    for i in range(len(a)):
        #Current sum is 0
        curSum = 0
        
        #Here j is the iterator
        for j in range(len(a)): #So this line says, for each item in len(a) do the following....
            curSum += abs(a[i] - a[j])   #Add the abs(a[j] minus a[j])  
            #^this seems wonky/wrong to me because that expression would always evalate to 0
            #So, I'll go ahead and change line 18 to:   curSum += abs(a[i] - a[j]) 
        if curSum < minimalSum: #If the curSum is less than the minimalSum then....
            minimalSum = curSum #Set the minimalSum to the curSum......
            indexOfMinimum = i  #Then set (aka identify) the indexOfMinimum as i

    print(a[indexOfMinimum])
    return a[indexOfMinimum] #The answer is a[indexOfMinimum]

solution([1,1,3,4])

