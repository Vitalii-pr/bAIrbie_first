def arrange(s):
    t=[]
    i=0
    while(len(t)<len(s)-1):
        if(i%2==0):
            t.append(s[i])
            t.append(s[len(s)-1-i])
        else:
            t.append(s[len(s)-1-i])
            t.append(s[i])
        i+=1
    if len(s)%2!=0:
        t.append(s[i])
    return t
