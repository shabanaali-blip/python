def rev(s):
    l=len(s)
    result=s[-1::-1]
    print("Reverse of the string is : ", result)
def Ucount(s):
    count=0
    for i in s:
        if i.isupper():
            count=count+1
    print("Number of uppercase letters = ",count)
def Lcount(s):
    count=0
    for i in s:
        if i.islower():
            count=count+1
    print("Number of lowercase letters = ",count)
def Pal(a):
    s=a.lower()
    l=len(s)
    r=s[-1::-1]
    if r==s:
        print("String is palindrome")
    else:
        print("String is not palindrome")
def Pan(s):
    a=s.lower()
    al="abcdefghijklmnopqrstuvwxyz"
    for i in al:
        if i not in a:
            return "String is not Pangram "
    return "String is pangram"
