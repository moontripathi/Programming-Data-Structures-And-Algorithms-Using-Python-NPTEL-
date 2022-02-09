# Function threesquares --------------------------------
def threesquares(n):
    i=0
    f=0
    a=8*i+7
    b=n-7
    if b%8==0:
        return False

    if n%4==0:
        while(a < (n/2)):
            if n % a != 0:
                i=i+1
                f=1
            if(f!=1):
                if n%a==0:
                    return False
            a=8*i+7
            f=0
        return True
    else:
        return True

# Function repfree -------------------------------------------

def repfree(st1):
    list_1 = list(st1.strip(" "))
    list_2 = set(list_1)
    if len(list_1) == len(list_2):
        return True
    else:
        return False

# function hillvalley ---------------------------------------
      
def hillvalley(list1):
    f=1
    if list1[0] > list1[1]:
        #print("Bye")
        for i in range(0,len(list1)-1):
            if list1[i] > list1[i+1]:
                if (f==1):
                    continue
                else:
                    return False
            else:
                f=0
        if f==1:
            return False
        else:
            return True
    else:
        #print("Hello")
        for i in range(0,len(list1)-1):
            if list1[i] < list1[i+1]:
                if (f==1):
                    continue
                else:
                    return False
            else:
                f=0
        if f==1:
            return False
        else:
            return True