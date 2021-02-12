def Uni(l):
    u=[]
    for i in l:
        if i not in u:
            u.append(i)
    for i in u:
        print(i,end=" ")
    print(" ")
def sq(l):
    s=[]
    for i in l:
        a=i*i
        s.append(a)
    for i in s:
        print(i,end=" ")