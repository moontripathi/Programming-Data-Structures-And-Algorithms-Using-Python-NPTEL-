##solution for week 3

# function 1
def remdup(list_1):
    list_2=[]
    for i in list_1:
        if i not in list_2:
            list_2.append(i)
        else:
            continue
    return list_2

#function 2 
def sumsquare(list1):
    (even1,odd1)=(0,0)
    for i in list1:
        if i % 2 == 0 :
            even1 = even1 + i*i
        else:
            odd1 = odd1 +i*i
    list2=[]
    list2.append(odd1)
    list2.append(even1)
    return list2

#function 3 
def transpose(m):
    h, w = len(m[0]), len(m)
    new = [[0 for x in range(w)] for y in range(h)]
    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            new[j][i]=m[i][j]
    return new
