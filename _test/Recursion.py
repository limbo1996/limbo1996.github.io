# 非递归方法求和
def listsum(numlist):
    theSum = 0
    for i in numlist:
        theSum = theSum + i
    return theSum
# 递归
def listsumRecursion(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsumRecursion(numlist[1:])
