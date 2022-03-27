def swapList(newList1):
    size = len(newList1)
     
    temp = newList1[0]
    newList1[0] = newList1[size - 1]
    newList1[size - 1] = temp
     
    return newList1

newList = [1,2,3,4]
 
print(swapList(newList))

def swapList2(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList

print(swapList2(newList))

def swapList3(list):
     
    get = list[-1], list[0]
     
    list[0], list[-1] = get
     
    return list

print(swapList3(newList))

def Reverse(lst):
    return [ele for ele in reversed(lst)]

print(Reverse(newList))



def Reverse3(lst):
    new_lst = lst[::-1]
    return new_lst

print(Reverse3(newList))
newList = [1,2,3,4]
def Reverse2(lst):
    lst.reverse()
    return lst

print(Reverse2(newList))