
from sys import setrecursionlimit


setrecursionlimit(10000000)
def ack(m: int, n: int)-> int:
    if m==0:return n+1
    if n==0:return ack(m-1, 1)
    return ack(m-1,ack(m, n-1))

print(ack(2,2))