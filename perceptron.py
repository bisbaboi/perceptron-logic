
alpha=1

def activation_function(yin):
    if yin>0:
        return 1
    if yin==0:
        return 0
    return -1
    


def yin_fun(w1,x1,w2,x2,b):
    return w1*x1+w2*x2+b

def wnew(wold,ti,xi):
    return wold+alpha*ti*xi

def bnew(bold,ti):
    return bold+alpha*ti


if __name__=="__main__":
    w1=0
    w2=0
    b=0
    count =0
    flag = 1
    while flag == 1:
        x1 = [-1,-1,1,1]
        x2 = [-1,1,-1,1]
        t = [-1,1,1,1]
        for i in range(len(x1)):
            yin=yin_fun(w1,x1[i],w2,x2[i],b)
            y=activation_function(yin)
            if y==t[i]:
                count+=1
                if count==len(x1):
                    flag = 0
                    break
            else:
                count = 0
                w1 = wnew(w1,t[i],x1[i])
                w2 = wnew(w2,t[i],x2[i])
                b = bnew(b,t[i])
        if flag == 0:
            break
        
    print(w1,w2,b)
    print (count)        
        
        
        
        
        
    
    
    
    
