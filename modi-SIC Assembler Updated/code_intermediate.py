#Intermediate File
fin =open("in.txt",'r')                     #reading in.txt file
inter =open("intermediate.txt",'w')         #will write in intermediate file
for i in fin.readlines():
    temp=i.strip().split('\t')[1:4]
    if (len(temp)>2):
        if (temp[0]!='.'):
            for y in temp:
                inter.write("%s\t" %y)
            inter.write("\n")
        else:
            continue
    else:
        continue 
fin.close()
inter.close()