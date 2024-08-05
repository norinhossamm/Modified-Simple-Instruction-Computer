#Location Counter
import math
interin=open("intermediate.txt","r")
out1=open("out_pass1.txt","w")
Mnemonic= ["ADD","AND","COMP","DIV","J","JEQ","JGT","JLT","JSUB","LDA","LDCH","LDL","LDX","MUL","OR","RD","RSUB","STA","STCH","STL","STSW","STX","SUB","TD","TIX","WD","FIX","FLOAT","HIO","NORM","SIO","TIO"]
Format= ["3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","1","1","1","1","1","1"]
counter=0
temp1= interin.readline().split('\t')
out1.write('-\t'+'\t'.join(temp1))
LOCCTR= hex(int(temp1[2],16))
start= LOCCTR                           #needed for end
for i1 in interin.readlines():
    temp2=i1.strip().split('\t')
    out1.write(LOCCTR+'\t'+''.join(i1))
    if(temp2[1]=="WORD"):
        LOCCTR=hex(int(LOCCTR,16)+(3))
    elif (temp2[1]=="RESW"):
        LOCCTR=hex(int(LOCCTR,16)+(int(temp2[2])*3))
    elif(temp2[1]=="RESB"):
            LOCCTR=hex(int(LOCCTR,16)+int(temp2[2]))
    elif(temp2[1]=="BYTE"):
        if(temp2[2][0]=="X"):
            LOCCTR=hex(int(LOCCTR,16)+int(math.ceil(((len(temp2[2])-3)/2))))
        elif(temp2[2][0]=="C"):
            LOCCTR=hex(int(LOCCTR,16)+((len(temp2[2])-3)*1))
    else:
        for j in Mnemonic:
            if (temp2[1]==j):
                LOCCTR=hex(int(LOCCTR,16)+int(Format[counter],16))
            else:
                counter+=1
    counter=0
interin.close()
out1.close()
#--------------------------------------------------------------
#Symbol Table
outp1=open("out_pass1.txt","r")
symb=open("symbTable.txt","w")
symb.write("Address\tLabel\n")
for i2 in outp1:
    temp3=i2.strip().split('\t')[0:2]
    if(temp3[0]!='-' and temp3[1]!='-'):
        symb.write(temp3[0]+"\t"+temp3[1]+'\n')
    else:
        continue
outp1.close()
symb.close()