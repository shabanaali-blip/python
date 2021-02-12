from listpop.S2lab11 import *
a=input("Enter a list: ")
b=a.split(",")
b=list(map(int,b))
print("Unique elements are : ",end=" ")
Uni(b)
print("Squares are: ",end=" ")
sq(b)