d=input("now enter an list")
e=list(map(int,d.split()))
print (e)
for i in range(len(e)):
    print(i)
    for j in range(i+1,len(e)):
        print(j)
        if(e[i]<e[j]):
            print(e[i],"<",e[j])
            e[i],e[j] = e[j],e[i]
            print(e[i],">",e[j])
        
print(e)        