#program to append content accepted from user to a file:
a=input("Enter the details: ")
f1=open("A.txt","a")
f1.write(a)
f1.close()