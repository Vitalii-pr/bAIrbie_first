def get_start_time(s, d):
    s_t=sum(s,[])+[['09:00','09:00'],['19:00','19:00']]
    result=[]
    for i in s_t:
        for k in s_t:
            if (s2t(i[1])>=s2t(k[1]) or s2t(i[1])<=s2t(k[0])-d):
                if k==s_t[-1]:result.append(i[1])
            else:break
    return sorted(result,key=s2t)[0] if len(result)!=0 and sorted(result,key=s2t)[0]!='19:00' else None

def s2t(s):
    s=s.split(':')
    return int(s[0])*60+int(s[1])
