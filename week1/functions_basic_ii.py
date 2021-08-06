def countDown(num):
    list = []
    for j in range (num, -1, -1):
        list += [j]
    return list
print(countDown(5))

def printReturn(list):
    print(list[0])
    return(list[1])
print(printReturn([10,20]))

def firstPlusLength(list):
    return(len(list) + list[0])
print(firstPlusLength([10,1,2,3,4,5]))

def valueGreaterThanSecond(list):
    newList = []
    if len(list) < 2:
        return False
    else:
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                newList.append(list[j])
    return(newList)
print(valueGreaterThanSecond([5,2,3,2,1,4]))
print(valueGreaterThanSecond([3]))

def lengthThatValue(size, value):
    newList = []
    for j in range(size):
        newList += [value]
    return newList
print(lengthThatValue(4,7))
print(lengthThatValue(6,2))