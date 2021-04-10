def knapsack(W,wt,value,n):
    profit=[]
    inbag=[]
    for i in range(n):
        profit.append(float(value[i]/wt[i]))
    while W>0 and n>0:
        max_index=profit.index(max(profit))
        profit.pop(max_index)
        if W<wt[max_index]:
            inbag.append(W)
            W=W-W
            wt[max_index]=wt[max_index]-W
        else:
            W=W-wt[max_index]
            inbag.append(wt[max_index])
            wt.pop(max_index)
        n=n-1
    return inbag

if __name__=="__main__":
    ttl_weight=50
    weights=[100,20,30]
    values=[1000,1,1]
    l = len(weights)
    print(knapsack(ttl_weight,weights,values,l))



