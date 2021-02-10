#Program to copy a text file to another

f1=open("A.txt","r")
f2=open("B.txt","w")
s=f1.read()
f2.write(s)
f1.close()
f2.close()