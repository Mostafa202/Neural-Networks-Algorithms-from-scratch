
store=[]
def get_targets(y):

    for i in range(len(y)):
        for j in range(len(y[0])):
            if y[i][j] not in store:
                store.append(y[i][j])
          
    return sorted(store)

    
#print(get_targets([[2,4,7,8]])[1])












