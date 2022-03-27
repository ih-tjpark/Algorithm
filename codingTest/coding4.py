tri = ["2????","??5?","?3?","4?","1"]


for i in range(len(tri)-1,0,-1):
    up = list(tri[i-1])

    down = list(tri[i])
    back=list(range(len(down)))

    back_temp=[]
    count=0
    while back:
        
        if count >=len(down):
            break

        for j in back:

            if up[j].isnumeric():

                if int(up[j])<=int(down[j]):

                    up[j+1]=str(int(down[j])-int(up[j]))
                else:
                    up[j+1] =str((int(down[j])+10) - int(up[j]))
        
            elif up[j+1].isnumeric():
                if int(up[j+1])<=int(down[j]):

                    up[j]= str(int(down[j])-int(up[j+1]))
                else:
                    up[j] = str((int(down[j])+10) - int(up[j+1]))
            
            else:
                back_temp.append(j)
        count+=1
        #print(back_temp)
        back = back_temp
            

        tri[i-1] = ''.join(up)
    
    
        
    
        #print(tri)
        



