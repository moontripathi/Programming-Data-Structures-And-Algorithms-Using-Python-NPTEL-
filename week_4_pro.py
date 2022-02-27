def orangecap(d):
    total={}
    #print(d['test1']['Pant'])
    max=0
    for k in d.keys():
        for ke in d[k].keys():
            total[ke]=0

            for match in d.keys():
                if ke in d[match].keys():
                    total[ke]=total[ke] + d[match][ke]
            
            if max < total[ke]:
                max=total[ke]
                player=ke

    t=(player,max) 
    return t
  
def addpoly(p1,p2):
    dic={}
    lst=[]
    for i in p1:
        dic[i[1]] = 0
    for i in p2:
        dic[i[1]] = i[0]
    for i in p1:
        dic[i[1]] = dic[i[1]] + i[0]

    for key, value in sorted(dic.items(),reverse=True):
        if value != 0:
            t1=(value,key)
            lst.append(t1)
    
    return lst