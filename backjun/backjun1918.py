import sys

cal_string =sys.stdin.readline()

t= False
g=0
pm = False
md = False
#(A+B)*C
alpha =''
cal = ''
g_cal =''
result=''
cal_result=''
final_result=''
for string in cal_string:

    #A-Z가 들어오면 적재
    #수식일때 
    #print(string)
    #print(md)
    if string.isalpha():
        alpha+=string
    
    elif string in ['-','+']:

        if md and not g:
            cal_result = g_cal+cal
            result += alpha + cal_result
            alpha=''
            g_cal=''
            cal=''
            md = False
            t= True
         
        if g>0:
            g_cal = g_cal + string 
        else:
            cal =  cal + string
    
    elif string in ['*','/']:

        if md and g>0:
            cal_result = g_cal+cal
            result += alpha + cal_result
            alpha=''
            g_cal=''
            cal=''
            md = False
            t= True

        if g>0:
            g_cal = string +g_cal
        
        else:
            cal = string + cal
        
        
        md = True


    elif string =='(':
        g +=1 
    
    elif string ==')':
        g =1
    
    if t:
        final_result = result+alpha+g_cal+cal
    
    else:
        final_result = alpha+g_cal+cal
    
    #print(final_result)

print(final_result)
    