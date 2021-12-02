def read():
    data = []
    f = open ('Day2\data.txt','r')
    text = f.readlines()
    for line in text:
        data.append(line.split())
    f.close()
    return data

def drive(data):
    j=0
    k=0
    forward=0
    for i in range(len(data)):
        if(data[i][0]=='forward'):
            j+=int(data[i][1])
            forward+=int(data[i][1])*k
        elif(data[i][0]=='down'):
            k+=int(data[i][1])
        elif(data[i][0]=='up'):
            k-=int(data[i][1])
    return forward*j
    
print(drive(read()))
#read()