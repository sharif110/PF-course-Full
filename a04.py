### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
def openLocks(lock,std): 
    if lock == 0 or std == 0:
        return 0
    if lock < 0 or std < 0:
        return None
    locks = [False]*lock
    for c in range(1,std+1):
        for d in range(1,lock+1):
            if d%c == 0:
                if locks[d-1] == True:
                    locks[d-1] = False
                else:
                        locks[d-1] = True
    true = 0
    for h in range(1,lock+1):
        if locks[h-1] == True:
            true = true +1
    return true

#### End OF MARKER





### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###
def mostTouchableLocker(lock,std):
    if lock == 0 or std == 0:
        return 0
    if lock < 0 or std < 0:
        return None
    locks = [False]* lock
    max_lock =[0]*lock
    for a in range(1,std+1):
        for b in range(1,lock+1):
            if b%a == 0:
                max_lock[b-1] = max_lock[b-1] +1
    mx = max_lock[0]
    max_val = 0
    for g in range(0,lock) :
        if max_lock[g] >= mx:
            mx = max_lock[g]
            max_val = g+1
    return max_val
#### End OF MARKER


