#reversed binary code number
import math
n=int(input())
k=(1<<int(math.log2(n))+1)-1
print(n^k)

"""input:10
output:5"""
