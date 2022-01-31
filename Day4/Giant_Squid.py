def read(total):
    num = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    data = []
    f = open ('Day4\ex.txt','r')
    input = f.readline().split(',')
    print(input[1])
    k=0
    l=0
    
    while l<total-2:
        text = f.readline().split()
        for i in range(5):
            text = f.readline().split()
            data.append(text)
        #for j in range(5):
            for i in range(5):
                #print(data[j][i])
                for aux in num:
                    #print(aux)
                    if(aux==int(data[0][i])):
                        #print(aux)
                        k+=1
                if(k==5):
                    break
                else:
                    k=0
        l+=1
    print(k)

    f.close() 
    return data
def tot():
    with open('Day4\ex.txt') as f:
        total = sum(1 for line in f)
    return total


read(tot())
#print(drive(read()))
#print(epsilon(drive(read())))