def read():
    data = []
    f = open ('Day3\data.txt','r')
    text = f.readlines()
    for line in text:
        data.append(line.split())
    f.close()
    return data

def drive(data):
    aux=0
    gamma = []
    while aux<12:
        j=0
        k=0
        for i in range(len(data)):
            if(data[i][0][aux]=='0'):
                j+=1
            else:
                k+=1
        if(j>k):
            gamma.append(0)
        else:
            gamma.append(1)
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

print(drive(read()))
print(epsilon(drive(read())))