#Object code
from code_pass1 import Mnemonic,start,LOCCTR
Opcode=["18","40","28","24","3C","30","34","38","48","00","50","08","04","20","44","D8","4C","0C","54","14","E8","10","1C","E0","2C","DC","C4","C0","F4","C8","F0","F8"]
interin1=open("intermediate.txt","r")
# symbin=open("symbTable.txt","r")
out2=open("out_pass2.txt","w")
counter1=0
for i2 in interin1.readlines():
    temp3=i2.strip().split('\t')
    if(temp3[1]=="START" or temp3[1]=="RESW" or temp3[1]=="RESB"):
        out2.write('\t'.join(temp3)+ "\t-\n")
    elif(temp3[1]=="WORD"):
        out2.write('\t'.join(temp3)+'\t'+str(hex(int(temp3[2],10))[2:]).zfill(6)+'\n')
    elif(temp3[1]=="BYTE"):
        if(temp3[2][0]=="X"):
            out2.write('\t'.join(temp3)+'\t'+temp3[2][2:-1]+'\n')
        elif(temp3[2][0]=="C"):
            # letters=''.join(hex(int(str(ord(char)),10))[2:] for char in temp3[2][2:-1])
            # print(letters)
            out2.write('\t'.join(temp3)+'\t'+''.join(hex(int(str(ord(char)),10))[2:] for char in temp3[2][2:-1])+'\n')
    else:
        for j1 in Mnemonic:
            if(temp3[1]==j1):
                if(temp3[1]=="RSUB"):
                    out2.write('\t'.join(temp3)+'\t'+Opcode[counter1]+"0000")
                elif(temp3[2][0]=="#"):
                    out2.write('\t'.join(temp3)+'\t'+hex(int(Opcode[counter1],16)+int("1",16))[2:]+str(hex(int(temp3[2][1:],10))[2:]).zfill(4))
                else:
                    out2.write('\t'.join(temp3)+'\t'+Opcode[counter1])
                    symbin=open("symbTable.txt","r")
                    for i3 in symbin.readlines():
                        temp4=i3.strip().split('\t')
                        #if(temp3[2][-2:]=="X" and temp3[2][:-2]==temp4[1]):
                        if(temp3[2].find(",X")!=(-1) and temp3[2][:-2]==temp4[1]):
                            out2.write(hex(int(temp4[0][2:],16)+int("8000",16))[2:])
                        elif(temp3[2]==temp4[1]):
                            out2.write(temp4[0][2:])
                out2.write('\n')
                symbin.close()
            else:
                counter1+=1
        counter1=0
interin1.close()
out2.close()
#--------------------------------------------------------------
#HTE record
pass2=open("out_pass2.txt","r")
pass1=open("out_pass1.txt","r")
hte = open("HTE.txt","w")
prog_length=hex(int(LOCCTR,16)-int(start,16))[2:]
line1_p1=pass1.readline().strip().split('\t')
begin=line1_p1[0]
line1_p2=pass2.readline().strip().split('\t')
while(len(line1_p1[1])<6):
    line1_p1[1]+="X"
hte.write("H."+line1_p1[1]+"."+start[2:].zfill(6)+"."+prog_length.zfill(6)+'\n')            # H-record

prog_end=LOCCTR                                                                             # T-record
size=0
limit=30
obj_code=""
line2_p1=pass1.readline().strip().split('\t')
t_start=line2_p1[0][2:].zfill(6)
for i4 in pass2.readlines():
    temp5=i4.strip().split('\t')
    line3_p1=pass1.readline().strip().split('\t')
    if(temp5[1]=="RESW" or temp5[1]=="RESB"):
        if(size!=0):
            hte.write("T."+t_start+"."+hex(int(str(size),10))[2:].zfill(2)+"."+obj_code+"\n")
            size=0
            del obj_code
            obj_code=""
            t_start=line3_p1[0][2:].zfill(6)
        else:
            t_start=line3_p1[0][2:].zfill(6)
    elif(size<limit):
        obj_code+=temp5[3]+"."
        if(len(line3_p1)<2):
            size+=int(prog_end,16)-int(line2_p1[0],16)
        else:
            size+=int(line3_p1[0],16)-int(line2_p1[0],16)
    else:
        hte.write("T."+t_start+"."+hex(int(str(size),10))[2:].zfill(2)+"."+obj_code+"\n")
        t_start=line2_p1[0][2:].zfill(6)
        size=0
        del obj_code
        obj_code=""+temp5[3]+"."
        if(len(line3_p1)<2):
            size+=int(prog_end,16)-int(line2_p1[0],16)
        else:
            size+=int(line3_p1[0],16)-int(line2_p1[0],16)
    if(len(line3_p1)<2):
        hte.write("T."+t_start+"."+hex(int(str(size),10))[2:].zfill(2)+"."+obj_code+"\n")
    line2_p1[0]=line3_p1[0]

hte.write("E."+start[2:].zfill(6)+"\n")                                                         # E-record