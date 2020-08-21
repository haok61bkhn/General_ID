import random
f=open("id.txt","w+") 
d=0
Max=1000000

def gen(i,s):
    global d,Max
    if(d==Max):return
    if(i==9):
        f.writelines(s+"\n")
        d+=1
    else:
        for j in range(1):
            x = random.randint(0,9)
            gen(i+1,s+str(x))

while(d<Max):
    gen(0,"")
        

