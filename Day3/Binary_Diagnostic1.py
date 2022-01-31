def read():
    data = []
    f = open ('Day3\ex.txt','r')
    text = f.readlines()
    for line in text:
        data.append(line.split())
    f.close()
    return data

def drive(data):
    aux=0
    gamma = []
    while aux<5:
        j=0
        k=0
        for i in range(len(data)):
            if(data[i][0][aux]=='0'):
                j+=1
            else:
                k+=1
        if(j>k):
            gamma.append('0')
        else:
            gamma.append('1')
        aux+=1
    return gamma

def epsilon(gamma):
    epsilon=[]
    for i in range(len(gamma)):
            if(gamma[i]==0):
                epsilon.append(1)
            else:
                epsilon.append(0)
    return epsilon

def oxygen(data,aux,gamma):
    f = open ('Day3\ex.txt','w')
    j=0
    print("a")    
    
    if(len(data)==2):
        print("b")
    else:
        for i in range(0):#range(len(data)):
            if(data[i][0][aux]==gamma[aux]):
                f.write(data[i][0])
        aux+=1
        f.close()
        oxygen(read(),aux,gamma)
    
    return data
#print(oxygen(read(),0,drive(read())))
#print(drive(read()))
#print(epsilon(drive(read())))
for i in range(2):
    print(len(read()))