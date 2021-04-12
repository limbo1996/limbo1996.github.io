"""
Author: limbo1996
Date: 2021-04-09 13:49:08
LastEditTime: 2021-04-09 14:04:01
FilePath: /limbo1996.github.io/_test/Recursion.py
"""
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
