#list 1
a=[0,1,2,3]
#list 2
b=[3,5,6,7]
#c for storing intersection value
c=[]
e=a+b
#d list for A-B difference
d=[]
#intersection peocess
for I in a:
   for j in b:
     if( I==j):
         c.append(a[I])

#difference
for j in e:
    if j not in b:
         d.append(a[j])

#set keyword for unique valur
c1=set(c)
d1=set(d)
j=c1
e=set(e)


#symmetrical difference of two set
for x in j:
    if x in e:
        e.remove(x)
print("union a and b:",set(a+b))
print("intersection a and b:",c1)
print("difference a and b:",d1)
print("symmetrical difference a and b:",e)
         
       
