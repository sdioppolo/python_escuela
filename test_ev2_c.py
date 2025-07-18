def q(m,z,a,b):
    m[a][b]=8
    c=int(2)
    while(c>=0):
        if(a<z-1 and b<z-1):
            if(m[a+1][b+1] == 0):
                a+=1
                b+=1
        elif(a<z-1):
            if(m[a+1][b-1]==0):
                a+=1
                b-=1
        elif(b>0 and a<z-1):
            if(m[a+1][b]==0):
                a+=1
        m[a][b]=8
        c-=1

def p(m,z):
    for i in range(z):
        print(m[i])
    print()

mat=[[1,0,1],
     [0,1,0],
     [1,0,1]]

p(mat, 3)
q(mat, 3, 0, 1)
p(mat, 3)
                
